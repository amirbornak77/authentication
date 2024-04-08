# Docs

# Autehntication 
### creating a virtualenv with virtualenv pacakge.
### pip install dajngo==4.2.
### django-admin startproject myproject.
### py manage.py startapp authentication.
### after overriding user hould creating models for kyc

## chaging template directory
### os.path.join(BASE_DIR, 'templates')

## register my autehntication app in INSTALLED_APPS 
### 'authentication.apps.AuthenticationConfig',


# User 
### overriding the default user by adding an app name account
### makemigrations and migrate