#!/bin/bash

rm -rf nashvillehotindexapi/migrations
rm db.sqlite3
python manage.py makemigrations nashvillehotindexapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata customers
python manage.py loaddata restaurants
python manage.py loaddata restaurantheat
python manage.py loaddata orders
python manage.py loaddata ratings
