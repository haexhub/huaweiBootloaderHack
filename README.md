# Huawei-honor-unlock-bootloader (Python 3)

## Summary

After closing the official EMUI website, which allowed you to retrieve the code to unlock the bootloader of Huawei/Honor phones, here is a python script to retrieve it by yourself.

It uses a bruteforce method, based on the Luhn algorithm and the IMEI identifier used by the manufacturer to generate the unlocking code.

The original version was developed by [SkyEmi](https://github.com/SkyEmie). I made some tweaks for saving attempts to file, because brutforcing is taking a **looooooong** time. I'm trying to hack my P20 Pro with this and there, Huawei installed another obstacle. You can only try 5 attempts for inserting the unlook key, than your phone will restart automatically. So I had to reboot in fastboot mode every 4 attempts. This increases the amount of time while trying, but couldn't find a better solution. 

## Instructions

### Connecting a device in ADB mode

1. Enable developer options in Android.

    * Android One: Go to Settings > System > About device and tap _Build number_ seven times to enable developer options.

2. Enable USB debugging in Android.

    * Android One: Go to Settings > System > Developer options and enable USB debugging.

3. Connect your device to the computer 

4. ``` 
    git clone 
    cd 
4. Wait for the application to detect your device. The device info should appear in the top left section.

## FAQ & Troubleshooting

**The application doesn't work. Is there anything I should have installed?**

Yes, it was developed in python so it needs it to run, version 3. You can install the latest version from [here](https://www.python.org/downloads/).

**The app on Windows doesn't detect my device even though it's connected and USB debugging is enabled. What could be the issue?**

Windows most likely doesn't recognise your device in ADB mode. Install the universal ADB drivers from [here](http://dl.adbdriver.com/upload/adbdriver.zip), reboot your PC and try again.
