#!/bin/bash

set -e

sudo apt-get install -y python3-pip
sudo -H pip install -U pip
sudo -H pip install virtualenv

virtualenv -p python3 ./venv
source ./venv/bin/activate
pip install django
pip install django-rest-framework

source ./runserver.sh
