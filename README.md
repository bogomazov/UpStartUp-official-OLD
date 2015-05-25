# UpStartUp-official
Platform for lean startup development.

## Installation

* `$ git clone git@github.com:bogomazov/UpStartUp-official.git`
* `$ mkvirtualenv upstartup-env`
* `$ cd upstartup/`
* `$ pip install -r requirements.txt`
* `$ bower install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

## Angular directory structure (in the project directory root):

* /static/javascripts/<ng_app_name>.config.js
* /static/javascripts/<ng_app_name>.js
* /static/javascripts/<ng_app_name>.routes.js
* /static/javascripts/<ng_module_name>/<ng_module_name>.module.js
* /static/javascripts/<ng_module_name>/controllers/<controller_name>.controller.js, …
* /static/javascripts/<ng_module_name>/directives/<directive_name>.directive.js, …
* /static/javascripts/<ng_module_name>/services/<service_name>.service.js, …
* /static/templates/<ng_module_name>/<ng_template_name>.html, …
* /templates/<django_template_name>.html, …
* /templates/javascripts.html
