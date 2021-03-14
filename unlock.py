import json
import time
import math
import sys
import subprocess

welcomeText = """
*****************************************************************************  
*         Unlock Huawei Bootloader - Made by Haex inspired by SkyEmie       *
*                                                                           *
*  Please enable USB DEBBUG and OEM UNLOCK if your device does not appear   *
*                                                                           *
*           Be aware of lossing all your data => do backup ;)               *
***************************************************************************** 
"""

###############################################################################

failedAttemptsFilename  = 'failedAttempts.json'
# if your device has a limit of false attempts before reboot
# otherwise set isLimitAttemptEnabled to false
limitAttempt            = 5
isLimitAttemptEnabled   = False
startingPoint           = 1000000000000000

###############################################################################

def getFailedAttemptsFromFile(filename = 'failedAttempts.json'):
  try:

    with open(filename, 'r') as file:
      array = json.load(file)
      if (type(array) == list):
        return set(array)
      else:
        return set([ ])
  
  except:
    return set([ ])


def writeFailedAttemptsToFile(filename = 'failedAttempts.json', failedAttempts = [ ]):
  startTime = time.time()
  with open(filename, 'w') as file:
    json.dump(failedAttempts, file)
    print('* saved file in {0} seconds *'.format(time.time() - startTime))


def algoIncrementChecksum(imei, checksum, genOEMcode):
  genOEMcode  += int(checksum + math.sqrt(imei) * 1024)
  return genOEMcode


def luhn_checksum(imei):
  def digits_of(n):
    return [int(d) for d in str(n)]
  digits      = digits_of(imei)
  oddDigits   = digits[-1::-2]
  evenDigits  = digits[-2::-2]
  checksum    = 0
  checksum    += sum(oddDigits)
  for i in evenDigits:
    checksum += sum(digits_of(i * 2))
  return checksum % 10


def tryUnlockBootloader(imei, checksum, failedAttempts = set([ ])):
  unlocked          = False
  algoOEMcode       = 1000000000000000
  countAttempts     = 0

  while(unlocked == False):
    countAttempts += 1

    while algoOEMcode in failedAttempts or algoOEMcode < startingPoint:
      algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)

    answer = subprocess.run(
      ['fastboot', 'oem', 'unlock', str(algoOEMcode)]
    , stdout = subprocess.DEVNULL
    , stderr = subprocess.DEVNULL
    ) 

    if answer.returncode == 0:
      unlocked = True
      return algoOEMcode
    else:
      failedAttempts.add(algoOEMcode)

    count = len(failedAttempts)
    print('* shot {0} with code {1} *'.format(count, algoOEMcode))
    
    # reboot in bootloader mode after limit of attempts is reached
    if count % (limitAttempt - 1) == 0 and isLimitAttemptEnabled == True:
      subprocess.run(
        ['fastboot', 'reboot', 'bootloader']
      , stdout = subprocess.DEVNULL
      , stderr = subprocess.DEVNULL
      )

    if (isLimitAttemptEnabled and count % 4 == 0) or (not isLimitAttemptEnabled and count % 100 == 0):
      writeFailedAttemptsToFile(failedAttemptsFilename, list(failedAttempts))

    algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)


def main(args = [ ]):
  print(welcomeText)

  subprocess.run(['adb', 'devices'])

  imei = int(args[1]) if len(args) > 1 else int(input('Type IMEI digit: '))
  checksum = luhn_checksum(imei)

  subprocess.run(
    ['adb', 'reboot', 'bootloader']
  , stdout = subprocess.DEVNULL
  , stderr = subprocess.DEVNULL
  )

  input('Press any key when your device is in fastboot mode\n')

  failedAttempts  = getFailedAttemptsFromFile(failedAttemptsFilename)
  codeOEM         = tryUnlockBootloader(imei, checksum, failedAttempts)

  subprocess.run(['fastboot', 'getvar', 'unlocked'])
  subprocess.run(['fastboot', 'reboot'])

  print('\n\nDevice unlocked! OEM CODE: {0}'.format(codeOEM))
  print('Keep it safe\n')
  input('Press any key to exit...\n')
  exit()
###############################################################################

if __name__ == '__main__':
  main(sys.argv)