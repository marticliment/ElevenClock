# ElevenClock

[![Downloads Badge](https://img.shields.io/github/downloads/martinet101/ElevenClock/total.svg?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases)
[![Downloads@Latest Badge](https://img.shields.io/github/downloads-pre/martinet101/ElevenClock/latest/total?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases/latest)
[![Issues Badge](https://img.shields.io/github/issues/martinet101/ElevenClock?style=for-the-badge)](https://github.com/martinet101/ElevenClock/issues)
[![Closed Issues Badge](https://img.shields.io/github/issues-closed/martinet101/ElevenClock?style=for-the-badge)](https://github.com/martinet101/ElevenClock/issues?q=is%3Aissue+is%3Aclosed)
[![Release Version Badge](https://img.shields.io/github/v/release/martinet101/ElevenClock?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases/latest)

![Eleven Clock demo](https://raw.githubusercontent.com/martinet101/SomePythonThings-Media/master/elevenclock/main.webp)

A taskbar clock for secondary taskbars on Windows 11. When microsoft's engineers were creating Windows 11, they forgot to add a clock on the secondary screen taskbar. So I did that. ElevenClock is a simple app which provides the same functionality as in windows 10 secondary taskbar clock.

For more info, make sure to check out those articles:

- Published on MS Answers forum and written by [@Sumitdhiman](https://github.com/Sumitdhiman): [https://answers.microsoft.com/en-us/windows/...](https://answers.microsoft.com/en-us/windows/forum/all/add-clock-to-the-second-display-in-windows-11/14ed24f5-b203-4bd7-a4e7-c4eb3539b042)
- Published on ElevenForum: [https://www.elevenforum.com/t/show-clock-on-all-taskbars-on...](https://www.elevenforum.com/t/show-clock-on-all-taskbars-on-all-displays-in-windows-11.1731/)
- Published on PythonAwesome: [https://pythonawesome.com/elevenclock-a-secondary-clock-for...](https://pythonawesome.com/elevenclock-a-secondary-clock-for-secondary-taskbars-on-windows-11/)

## Table of contents

- [ElevenClock](#elevenclock)
  - [Table of contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Download from](#download-from)
  - [Known Issues](#known-issues)
  - [Screenshots](#screenshots)

## Features

- It supports all system locales and time formats (they are pulled from the OS)*
- It shows in all displays except in the primary one (Because you have the default system clock)
- It supports dark and light theme
- It has a hide button to prevent annoying on full-screen
- It imitates Windows 11's taskbar clock animation on hover
- It supports taskbars on the top of the screen
- It supports seconds enabling via locale or regedit (windows 11's default clock can't do that)
- ElevenClock downloads and installs updates automatically, so you don't have to
- Clicking the clock shows/hides the notifications and calendar panel
- Correct alignment and size on HiDPi displays (100%, 200%, 300%) AND on fractional HiDPI displays(125%, 150%, 175%, 250%, etc.)*
- Correct alignment and size on Different-scaled monitors (Display1: 100%, Display2: 150%, Display3: 225%, etc.)*
- The clock updates the time each second, so you won't see different times across all your taskbars
- The clock also adjusts itself automatically when (dis)connecting monitors
- Automatically starts at login

## Installation

 1. Download the lastest version from [SomePythonThings](https://www.somepythonthings.tk/programs/elevenclock/#downloadSection) or from [Github Releases](https://github.com/martinet101/ElevenClock/releases)
 2. Open the installer and bypass Windows Defender SmartScreen: Click on more info and then on run:
     2.1.  Click on "More info":
     ![Defender Smart Screen Installation Screen](https://github.com/martinet101/ElevenClock/blob/main/media/smartscreen1.jpg?raw=true)
     2.2. Click on "Run anyway":
     ![Defender Smart Screen Run Anyway Screen](https://github.com/martinet101/ElevenClock/blob/main/media/smartscreen2.jpg?raw=true)
 3. Install the program as normal:![Installer](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_7.png?raw=true)
 4. The clock should start automatically when the installation is finished.

   **TIP: Clicking four times on the clock will show this webpage*

## Download from

MajorGeeks: [https://m.majorgeeks.com/files/details/elevenclock.html](https://m.majorgeeks.com/files/details/elevenclock.html)
OlderGeeks: [https://www.oldergeeks.com/downloads/file.php?id=3802](https://www.oldergeeks.com/downloads/file.php?id=3802)
SoftPedia: [https://www.softpedia.com/get/Desktop-Enhancements/Clocks-Time-Management/ElevenClock.shtml](https://www.softpedia.com/get/Desktop-Enhancements/Clocks-Time-Management/ElevenClock.shtml)
Github Releases: [https://github.com/martinet101/ElevenClock/releases/latest](https://github.com/martinet101/ElevenClock/releases/latest)
SomePythonThings: [https://www.somepythonthings.tk/programs/elevenclock/](https://www.somepythonthings.tk/programs/elevenclock/)

## Known Issues

- For issues with the clock appearing at the middle of the screen, read [Issue #40 (comment)](https://github.com/martinet101/ElevenClock/issues/40#issuecomment-939523493)
- For issues with the clock missing on a third monitor, i'm aware of that and i'm working on it. Please DO NOT submit more issues about this

## Screenshots

Elevenclock on 100% DPI: ![100%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_1.png?raw=true)
Elevenclock on 125% DPI: ![125%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_2.png?raw=true)
Elevenclock on 150% DPI: ![150%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_3.png?raw=true)
Elevenclock on 175% DPI: ![175%](https://github.com/martinet101/ElevenClock/blob/main/media/elevenclock_4.png?raw=true)
