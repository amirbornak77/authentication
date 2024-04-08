# Docs

# Autehntication 
### creating a virtualenv with virtualenv pacakge.
### pip install dajngo==4.2.
### django-admin startproject myproject.
### py manage.py startapp authentication.
### after overriding user hould creating models for kyc
### for migrations you need to install pillow this package is used for ImageField 
### then makemigrations and migrate 

# templates for kyc
### creating base.html and authentication folder for kyc
### base.html is used for every element that repeats such as header and footer we write it once

### in the authentication folder inside the templates I'm gonna create a file named register.html for first step of authentication

## chaging template directory
### os.path.join(BASE_DIR, 'templates')

## register my autehntication app in INSTALLED_APPS 
### 'authentication.apps.AuthenticationConfig',


# User 
### overriding the default user by adding an app name account
### makemigrations and migrate