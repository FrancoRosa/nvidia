#!/bin/bash

pkill -f gphoto2 & \
sleep 2 && \
gphoto2 --set-config=5013=32773 && \
sleep 2 && \
source ~/Documents/roich-360/.ultra/bin/activate && \
python ~/Documents/roich-360/ftest.py
