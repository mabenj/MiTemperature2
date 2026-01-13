#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

#uncomment following line to use in python virtual environment
source venv/bin/activate

./MiTemperature2.py --watchdogtimer 5 --callback sendToIoTPlatform.py --callback-interval 3600 --battery

# crontab -e
# @reboot sleep 60 && /home/pi/git/MiTemperature2/start.sh >> /home/pi/git/MiTemperature2/cron.log 2>&1

