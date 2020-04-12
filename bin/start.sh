#!/bin/bash

/opt/bin/start-selenium-standalone.sh &
sleep 2
cd ~
python3 -m pytest