# Project Title

PyJs
  
## Prerequisites

    Python 3.6.9

### Installing

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

You'll need to have a virtual environment installed on your machine

    pip3 install virtualenv

Setup virtual environment

    virtualenv env_pyjs

Activate virtual environment

    source env_pyjs/bin/activate

Install the requirements

    pip install -r requirements

Go to the folder PyJs/settings and comment out the production_settings and uncomment the development settings so you can use the development_setting to run this project locally on your machine.

The development_setting uses SQlite while production uses Postgres.

Make migrations, createsuperuser and run the server

    python manage.py makemigrations account polls
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

This project also has docker configured. So if you choose to run it with Docker, make sure yoou have docker and docker-compose install and properly setup on your system.

To run with docker

    docker-compose up

if you are on linux and the command above doesn't work, try the one below

    sudo docker-compose up

### Built With

    Python - Programming language used
    Django-rest-framework - The web framework used
    django-rest-swagger - Used to generate documentation for all the endpoints

### Important notes

The media files are being served through cloudinary, you will need to setup a cloudinary account if you dont have one, but if you do, the create a .env file in the root of this project and add the following

    CLOUD_NAME = "your cloud name"
    API_KEY = "your api key"
    API_SECRET = "your secret key"

### Authors

Baron Chibuikem (A fullstack software developer)
