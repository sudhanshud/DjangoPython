#! /bin/bash
echo "Start Test Setup"
#pip install virtualenv
#virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python datamigration.py
python manage.py runserver &
