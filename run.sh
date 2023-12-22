#!/bin/bash
echo Checking if you have python
sleep 1
command -v python3 >/dev/null 2>&1 && echo Python 3 is installed

sleep 2
echo Activating virtual Enviroment 
python3 -m venv .venv
source .venv/bin/activate
echo $venv

sleep 2
echo Installing External Packages
pip3 install colored
pip3 install pytest

sleep 2
echo Compiling main.py to check for Syntax Errors
python3 -m py_compile main.py

sleep 5
echo Running Game

sleep 2
python3 main.py

sleep 15