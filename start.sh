#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

#uncomment following line to use in python virtual environment
source venv/bin/activate

./MiTemperature2.py --watchdogtimer 5 --callback sendToIoTPlatform.py --callback-interval 3600 --battery

