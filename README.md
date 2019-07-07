# HoodWatch
A web application which allows users to connect to various neigborhoods

## User stories

The user should be able to:

+ [x] Sign in with the application to start using.
+ [x] Set up a profile about me and a general location and my neighborhood              name.
+ [x] Find a list of different businesses in my neighborhood.
+ [x] Find Contact Information for the health department and Police                     authorities near my neighborhood.
+ [x] Create Posts that will be visible to everyone in my neighborhood.
+ [x] Change My neighborhood when I decide to move out.
+ [x] Only view details of a single neighborhood.

## Prerequisites
+ [x] Python3.6.7

## Installation
To install, follow the following instructions;

```bash
    $ https://github.com/Doktatech/HoodWatch.git
    $ cd HoodWatch
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver
```
## Setting up the  enviroment variables
create a .env file in the root folder and add the following variables in it.

```bash
    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

## Known Bugs
	There are no known bugs as of the latest update

## Technology used

* [Python3.6.7](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Bootstrap](https://www.getbootstrap.com/)
* [Heroku](https://heroku.com)
 

## License ([MIT License](https://github.com/Doktatech/HoodWatch/blob/master/LICENSE))
This project is licensed under the MIT Open Source license, (c) [Rewel Kinyanjui](https://github.com/Doktatech)
