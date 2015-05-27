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

## Compile first page front-end
* `templates/index.html` - page that django serve all the time
* `templates/javascripts.html`- put here all javascript/angularjs libs. It will compress all js files into one.
* `templates/stylesheets.html`- put here all css libs. It will compress all css files into one.
* `templates/navbar.html` - template will be put instead of `{% include 'navbar.html' %}` in `index.html` while rendering
* In upstartup/settings.py put any external library to use in front-end in here:
BOWER_INSTALLED_APPS = (
    'angularjs',
    'jquery',
    'bootstrap',
    'angular-xeditable'
)
* then python manage.py bower install to collect all libs in `static/libs/bower_components`

