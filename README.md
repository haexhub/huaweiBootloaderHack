# Huawei-unlock-bootloader

## Summary

After closing the official EMUI website, which allowed you to retrieve the code to unlock the bootloader of Huawei/Honor phones, here is a python script to retrieve it by yourself.

It uses a bruteforce method, based on the Luhn algorithm and the IMEI identifier used by the manufacturer to generate the unlocking code.

The original version was developed by [SkyEmi](https://github.com/SkyEmie). I made some tweaks for saving failed attempts to file, because brutforcing is taking a **looooooong** time. I'm trying to hack my P20 Pro with this. Because Huawei placed another obstacle in th way, as you have 5 attempts for inserting the unlook key, than your phone will restart automatically. So I have to reboot in fastboot mode every 4 attempts. This increases the amount of time while trying, but couldn't find a better solution. 

## Instructions

### Connecting a device in ADB mode

1. Enable developer options in Android at your phone.

    * Go to Settings > System > About device > tap _Build number_ seven times to enable developer options.

2. Enable USB debugging in Android.

    * Go to Settings > System > Developer options and enable USB debugging.

3. Connect your device to the computer 

4. ``` 
    git clone https://github.com/haexhub/huaweiBootloaderHack.git
    cd huaweiBootloaderHack
    python3 unlock.py <IMEI>
    ```
4. Make a few cups of coffee or tea => sleep => repeat :D

## FAQ & Troubleshooting

**The application doesn't work. Is there anything I should have installed?**

Yes, it was developed with python3 so it needs it to run. You can install the latest version from [here](https://www.python.org/downloads/).
You also need [fastboot](https://www.droidwiki.org/wiki/Fastboot_(Tool)) installed on your system!
