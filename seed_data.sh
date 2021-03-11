#!/bin/bash

rm -rf nashvillehotindexapi/migrations
rm db.sqlite3
python manage.py makemigrations nashvillehotindexapi
python manage.py migrate
python manage.py loaddata eaters
python manage.py loaddata heats
python manage.py loaddata heatrestaurant
python manage.py loaddata notes
python manage.py loaddata orders
python manage.py loaddata ratings
python manage.py loaddata restaurants
