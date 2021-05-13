## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)

## General info
This project is simple app to collect data of users, who want to register for various trainings.
	
## Technologies
Project is created with:
* Python version: 3.8
* Django version: 3.2.1
* django-jazzmin: 2.4.6

	
## Features
Training object is created using admin panel. The unique link for the training is created. 
This link can be placed on a webpage or send to interested people by e-mail. The link directs to a RODO form, which collects following data:
- user's name and surname
- user's phone number and e-mail
- user's address
- user's permissions to collect and proceed theirs data

When the user posts theirs data, the information is saved in database, an e-mail is sent to the user with unique url generated.
After opening confirmation link from the email, user's profile is marked in database as confirmed and theirs data is sent to training's e-mail address.

	
## Setup
To run this project, do folowing steps:
- install requirements from reqirements.txt
- fill the required data in local_settings.py:
    - e-mail and password for your gmail account - it is used to send e-mails
    - allow 'less secure app access' in your gmail settings: https://myaccount.google.com/security?pli=1
    - (optional) database settings - sqlite db is default
    - (optional) BASE_URL - default is django development server at http://127.0.0.1:8000
- perform migration
- create superuser: `python manage.py createsuperuser`
- create training object using django admin
- the link to training's form is `BASE_URL` from settings + /join/ + training url generated during object creation, e.g.: http://127.0.0.1:8000/join/XXXXXXXXXX
