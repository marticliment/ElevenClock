# ElevenClock
[![Downloads Badge](https://img.shields.io/github/downloads/martinet101/ElevenClock/total.svg?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases)
[![Downloads@2.3](https://img.shields.io/github/downloads/martinet101/ElevenClock/latest/total?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases/latest) 
[![Issues Badge](https://img.shields.io/github/issues/martinet101/ElevenClock?style=for-the-badge)](https://github.com/martinet101/ElevenClock/issues)
[![Closed Issues Badge](https://img.shields.io/github/issues-closed/martinet101/ElevenClock?style=for-the-badge)](https://github.com/martinet101/ElevenClock/issues?q=is%3Aissue+is%3Aclosed)
[![Release Version Badge](https://img.shields.io/github/v/release/martinet101/ElevenClock?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases/latest)


![Eleven Clock demo](https://raw.githubusercontent.com/martinet101/SomePythonThings-Media/master/elevenclock/main.webp)

A taskbar clock for secondary taskbars on Windows 11. When microsoft's engineers were creating Windows 11, they forgot to add a clock on the secondary screen taskbar. So I did that. ElevenClock is a simple app which provides the same functionality as in windows 10 secondary taskbar clock.

For more info, make sure to check out this article published on MS Answers forum and written by [@Sumitdhiman](https://github.com/Sumitdhiman): [https://answers.microsoft.com/en-us/windows/...](https://answers.microsoft.com/en-us/windows/forum/all/add-clock-to-the-second-display-in-windows-11/14ed24f5-b203-4bd7-a4e7-c4eb3539b042)

## Support the dev:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://ko-fi.com/martinet101)
<br>
## Table of contents

- [ElevenClock](#elevenclock)
  - [Table of contents](#table-of-contents)
  - [Translating ElevenClock](#translating-elevenclock-to-other-languages)
  - [Features](#features)
  - [Planned Features](#planned-features)
  - [Installation](#installation)
  - [Download from](#download-from)
  - [Known Issues](#known-issues)
  - [Frequently Asked Questions](#frequently-asked-questions)
  - [Screenshots](#screenshots)

## Translating ElevenClock to other languages
See [TRANSLATION.md](https://github.com/martinet101/ElevenClock/blob/main/TRANSLATION.md)

## Easy installation:

Press <kbd>Win</kbd>+<kbd>R</kbd> type `cmd` and press <kbd>Enter</kbd>. Then, copy and paste `winget install ElevenClock`. Finally press <kbd>Enter</kbd>. ElevenClock will be installed automatically. 

## Features

- It supports all system locales and time formats (they are pulled from the OS)*
- It shows in all displays except in the primary one (Because you have the default system clock)
- It supports dark and light theme
- It has a hide button to prevent annoying on full-screen
- It imitates Windows 11's taskbar clock animation on hover
- It supports taskbars on the top of the screen
- It supports moving the clock to the left of the screen
- It supports different system integrations, like hiding when RDP is active
- It is compatible with small taskbars
- It supports taskbar customizations like Start11
- It supports seconds enabling via locale or regedit (windows 11's default clock can't do that)
- ElevenClock downloads and installs updates automatically, so you don't have to
- Clicking the clock shows/hides the notifications and calendar panel
- Correct alignment and size on HiDPi displays (100%, 200%, 300%) AND on fractional HiDPI displays(125%, 150%, 175%, 250%, etc.)*
- Correct alignment and size on Different-scaled monitors (Display1: 100%, Display2: 150%, Display3: 225%, etc.)*
- The clock updates the time each second, so you won't see different times across all your taskbars
- The clock also adjusts itself automatically when (dis)connecting monitors
- Automatically starts at login

## Supported languages
 - Catalan
 - English
 - French
 - German
 - Spanish
 - Polish
 - Russian
 - Turkish
 - Italian
 - Dutch
 - Norwegian
 - Korean
 - Vietnamese
 - Greek

### Languages coming in the next version:
 - None by the moment

## Planned features
 - [ ] You say!

## Installation

 1. Download the lastest version from [SomePythonThings](https://www.somepythonthings.tk/programs/elevenclock/#downloadSection) or from [Github Releases](https://github.com/martinet101/ElevenClock/releases)
 2. Open the installer and bypass Windows Defender SmartScreen: Click on more info and then on run:<br>
     2.1.  Click on "More info":<br>
     ![Defender Smart Screen Installation Screen](https://github.com/martinet101/ElevenClock/blob/main/media/smartscreen1.jpg?raw=true)<br><br>
     2.2. Click on "Run anyway":<br>
     ![Defender Smart Screen Run Anyway Screen](https://github.com/martinet101/ElevenClock/blob/main/media/smartscreen2.jpg?raw=true)<br><br>
 3. Install the program as normal:<br>![Installer](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_7.png?raw=true)<br><br>
 4. The clock should start automatically when the installation is finished.

   **TIP: Clicking four times on the clock will show this webpage*

## Download from

MajorGeeks: [https://m.majorgeeks.com/files/details/elevenclock.html](https://m.majorgeeks.com/files/details/elevenclock.html)<br>
OlderGeeks: [https://www.oldergeeks.com/downloads/file.php?id=3802](https://www.oldergeeks.com/downloads/file.php?id=3802)<br>
SoftPedia: [https://www.softpedia.com/get/Desktop-Enhancements/Clocks-Time-Management/ElevenClock.shtml](https://www.softpedia.com/get/Desktop-Enhancements/Clocks-Time-Management/ElevenClock.shtml)<br>
Github Releases: [https://github.com/martinet101/ElevenClock/releases/latest](https://github.com/martinet101/ElevenClock/releases/latest)<br>
SomePythonThings: [https://www.somepythonthings.tk/programs/elevenclock/](https://www.somepythonthings.tk/programs/elevenclock/)<br>

## Known Issues

 - ElevenClock might be reposted as a potential virus or it might be quarentined (Most of the users used Mcafee)
 
## Frequently asked questions

**Q: The clock shows over fullscreen**<br>
A: Enable fullscreen hiding in settings<br>

**Q: The clock shows over RDP sessions**<br>
A: Enable RDP hiding in settings (it may consume more CPU)<br>

**Q: Can ElevenClock be in my language?**<br>
A: Yes, just take a look to [TRANSLATION.md](https://github.com/martinet101/ElevenClock/blob/main/TRANSLATION.md)<br>

**Q: My antivirus is telling me that ElevenClock is a virus/My antivirus is uninstalling ElevenClock/My browser is blocking ElevenClock download**<br>
A: Just whitelist ElevenClock on the antivirus quarantine box/antivirus settings<br>

**Q: The clock shows seconds when the "Show Seconds" settings is disabled**<br>
A: Check that yiu don't have seconds set in your regional settings and disable seconds following this [article's instructions](https://www.howtogeek.com/325096/how-to-make-windows-10s-taskbar-clock-display-seconds/) (Other guides might not work)<br>

**Q: ElevenClock does not show the correct time zone when time zone is changed**<br>
A: Just restart ElevenClock (Right-click clock -> Restart ElevenClock)<br>

**Q: The main clock does not get modified when enabling seconds, etc.**<br>
A: ElevenClock can't modify or update  the main clock due to Windows 11's restrictions.

## Screenshots

Elevenclock on 100% DPI: ![100%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_1.png?raw=true)
Elevenclock on 125% DPI: ![125%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_2.png?raw=true)
Elevenclock on 150% DPI: ![150%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_3.png?raw=true)
Elevenclock on 175% DPI: ![175%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_4.png?raw=true)
ElevenClock settings: <br>![Settings](https://user-images.githubusercontent.com/53119851/137625716-e0d9e5b2-d188-4a76-8146-77061970b78f.png)
![Settings2](https://user-images.githubusercontent.com/53119851/137625725-08bd6408-abcc-4c87-9be6-bbb1dad5ed75.png)
![Settings3](https://user-images.githubusercontent.com/53119851/137625731-08594ba7-9d66-4add-82d1-2a64400293df.png)



