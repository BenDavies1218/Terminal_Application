#!/bin/bash/python3


# Activate Virtual Enviroment
echo Activating virtual Enviroment 
python3 -m venv .venv
source .venv/bin/activate
echo $VIRTUAL_ENV


# Install Packages
echo Installing External Packages
pip3 install colored
pip3 install -U pytest