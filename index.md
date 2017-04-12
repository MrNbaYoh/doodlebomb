## ![Image](http://i.imgur.com/2rezJxz.png) Doodlebomb

Doodlebomb is a userland exploit for the 3ds application Swapdoodle. It allow one to access [the Homebrew Launcher](http://smealum.github.io/3ds/) through the game.

### Requirements

To be able to install doodlebomb you need : 
* a 3ds on firmware <= 11.4
* a digital copy of Swapdoodle (v1.1.1) (available for free on the eshop)
* a way to boot [the Homebrew Launcher](http://smealum.github.io/3ds/) OR a friend who already have doodlebomb installed

### Installation

#### With [the Homebrew Launcher](http://smealum.github.io/3ds/)

1. Make sure you're the author of the latest created letter (it will be overwritten). If you have no idea about that, just create a new letter and make sure you do not receive any letter afterwards.
2. Download the [doodlebomb_installer](https://github.com/MrNbaYoh/doodlebomb_installer/releases/) archive and extract its content to the /3ds folder on your SD card.
3. Launch the installer through the HBL and follow the instructions.
4. Go to the final step.

#### Without [the Homebrew Launcher](http://smealum.github.io/3ds/)

1. Make sure you can receive special letters (turn on the option in the game settings)
2. Ask a friend who already have doodlebomb installed to just send you its own doodlebomb letter (only the letter installed via the homebrew installer can be sent).
3. Go to the final step.

#### Final step

1. Get the [doodlebomb archive](https://github.com/MrNbaYoh/doodlebomb/releases/) and copy the files according to your region to /doodlebomb/ on your SD card (you may have to manually create this folder).
2. Download the [otherapp payload](http://smealum.github.io/3ds/) corresponding to your region/console/firmware etc.
3. Copy the otherapp payload to the /doodlebomb folder and rename it "otherapp.bin".

### How to use doodlebomb

To access the HBL with doodlebomb, just try to open the doodlebomb letter in swapdoodle, it should run the hax payload.

### Troubleshooting

**When I try to open the doodlebomb letter, a message is displayed...**
As stated in this error message you probably forgot to put the rop.bin file in the /doodlebomb folder. If it still occurs after checking the file are present in required location, exit the game and try again. If this error persists, ask for help.

**When I try to run the exploit the game just crashes...**
Firstly check that all the required files are actually in the /doodlebomb folder. Then verify the region of the files, maybe you've just copied the wrong file for another region. Moreover some random crashes may occur sometimes, just reboot and try again. If the issue persists, ask for help.

### I don't have any friend and I can't run the HBL, what can I do ?

You can probably find some friends and people that would be glad to help on the internet through forums and social network. Try to use the [#GetDoodlebomb](https://twitter.com/hashtag/GetDoodlebomb) hashtag on twitter to find people that are able to help you.


### Thanks
* [Vegaroxas](https://github.com/VegaRoXas) : ropdb base, pyrop bug finding, exploit name and many other things
* [d3m3vilurr](https://github.com/d3m3vilurr) : help for JAP version
* [smealum](https://github.com/smealum) : do I really need to enumerate all the reasons ?
* ChampionLeake789 : tester
