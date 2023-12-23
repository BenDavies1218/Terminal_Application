#!/bin/bash
echo Checking if you have the minimum required version of Python
sleep 2

function python_version () {
    if command -v python3 >/dev/null 2>&1 ; then
        echo Python 3 is installed this will suffice
    else
        echo Application requires at least python 3
        read -p "Would you like to install it?" install
        if install == 'yes' ; then
            sudo apt-get install python3
        else
            echo Cant run Application
            exit
        fi
    fi
}
python_version

echo Installing Dependancies
source Dependancies.sh && sleep 2

echo Running Game && sleep 4
python3 main.py