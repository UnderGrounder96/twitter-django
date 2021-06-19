#!/bin/sh

apt update
apt install -y python3 python3-pip python3-venv sqlite3
apt clean

# python3 -m venv venv
# source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver "0.0.0.0:${PORT}"
