#!/bin/bash

python manage.py makemigrations

python manage.py makemigrations SystemsApp

python manage.py migrate