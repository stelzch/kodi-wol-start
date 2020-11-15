#!/bin/bash

while true; do

returnval=1
while [[ $returnval != 0 ]]; do
  python3 /home/pi/Scripts/wolscript.py
  returnval=$?
done
echo Received WOL, starting KODI

sudo -u pi kodi
echo KODI terminated

done
