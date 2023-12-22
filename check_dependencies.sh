#!/bin/bash

# check if python installed
echo Checking if you have python
sleep 1
command -v python3 >/dev/null 2>&1 && echo Python 3 is installed

sleep 2
echo Activating virtual Enviroment 
python3 -m venv .venv
source .venv/bin/activate

sleep 2
echo Installing External Packages
pip3 install colored
pip3 install pytest