# UpStartUp-official
Platform for lean startup development.

## Installation

* `$ git clone git@github.com:bogomazov/UpStartUp-official.git`
* `$ virtualenv upstartup-env`
* `$ cd upstartup/`
* `$ pip install -r requirements.txt`
* `$ bower install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

## Front-end

* `gulp` or `gulp build` to build an optimized version of your application in `/dist`
* `gulp serve` to launch a browser sync server on your source files
* `gulp serve:dist` to launch a server on your optimized application
* `gulp test` to launch your unit tests with Karma
* `gulp test:auto` to launch your unit tests with Karma in watch mode
* `gulp protractor` to launch your e2e tests with Protractor
* `gulp protractor:dist` to launch your e2e tests with Protractor on the dist files
