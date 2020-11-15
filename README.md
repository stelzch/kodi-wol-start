# Kodi Wake-on-LAN

## Purpose
I run the Kodi media center on a Raspberry Pi 3 in my living room. The Pi is simultaneously used as a sort of microserver, so to keep the CPU load low, Kodi should only be run when it is actively used.

The remote app [Kore](https://github.com/xbmc/Kore) includes a Wakeup-Button that sends a [Wake-on-LAN](https://en.wikipedia.org/wiki/Wake-on-LAN) packet to the Pi. Normally it is used to wake up the computer from a sleep mode, but this project utilizes the WoL-packet to start Kodi.

## Installation

Put `kodi-starter.sh` and `wolscript.py` in the `/home/pi/Scripts` directory.
Copy `wolkodi.service` to `/etc/systemd/system`.

Then you can simply run

```
sudo systemctl enable wolkodi.service
sudo systemctl start wolkodi.service
```

to enable Kodi-execution on WoL-packet.

## wolscript.py
This script file could also be used for similar projects. It listens for the WoL-magic-packet and returns with exit code 0 upon reception.