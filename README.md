# nitro-remote
Software to turn a raspberry pi into a device that can communicate with a IS-Nitro.

Make sure the files located in /src are placed in /boot/firmware/ on the raspberry pi.

Also make sure the USB-drivers for ortin to comunicate with the IS-NITRO-EMULATOR are installed on the pi.

pinout for numpad
GPIO21: Full hardware reset
GPIO25: Soft reset
GPIO18: Turn slot 1 on/off
GPIO2:  Turn slot 2 on/off

GPIO20: load /boot/firmware/rom.nds
GPIO24: enable av-out
GPIO15: configure upper screen
GPIO3:  configure lower screen

GPIO16: NC
GPIO23: NC
GPIO14: NC
GPIO4:  NC