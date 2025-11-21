# Development Notes

- the dev. server that runs after `python manage.py runserver` command should only be used before deployment

- projects vs. apps

  - apps are web applications that does something (blog app, poll app, ...)
  - project is a collection of (config + apps) for a particular website
  - project contains multiple apps, and an app can be in multiple projects

- use `include()` to include urlConf of other apps

- the `migrate` command runs only migrations of apps mentioned in `INSTALLED_APPS`

- model: single definitive source of information about your data. it contains fields and behaviors of the data

- to make models of your app to be mapped into db. add your app to `INSTALLED_APPS`. then `makemigrations` and `migrate`

  - `makemigrations`: tells django that we've changed the models. and we need to store those changes as a migration
  - `migrate`: applies all migrations that are not applied

- if you want to see the sql behind a migration file. use `sqlmigrate` command

  - `python manage.py sqlmigrate polls 0001`

- run `python manage.py shell` to use the API provided by django (auto imports models)

- when a request is made to a specific url. django loads the **_project.urls_** file. then find **_urlpatterns_** variable, and traverse the patterns in order

  - if a pref is matching a certain app urlCONF. it strips the pref and send the remaining part to that app urlCONF

- having several template files with the same name `index.html` will prevent django from recognizing them, because it returns the first matching template name

  - that's why we may use the django convention of putting templates in `app_name/templates/app_name/file.html`

  - same for static files `static/app_name/file.(css, js, png)`

- the `render(request, view_path, [context])` method is a shortcut of loading a template and rendering it within a `HttpResponse` returned from a view

- the `get_object_or_404(model, args)` method is a shortcut of getting an instance object from that model if one exists matching the given _args_ or raising `Http404` in the corresponding view function. it pass the _args_ to the model's manager method `get()`
  - it returns the object or raise a `Http404`
  - `get_list_or_404()` do the same, but uses `filter()` instead of `get()`
- you should always return a `HttpResponseRedirect` after dealing with POST data

- generic views abstract common patterns (listing objects, get a detailed object template)

  - each view needs to know the
    - **model** \ **get_queryset()**: it will be acting upon
    - **template_name**
    - **context_object_name**
    - **permission_classes**

- the default context_object_name for a ListView is the model_name_list (question_list)

- **_automated tests_** is letting the system do the testing work for you. you create a set of tests and change the code, and you run the tests to check that the code is still working as expected

- test classes should subclass the `django.test.TestCase` class
- python look for tests in any file with name starting with **_test_**

- to run the tests of an application, run `python manage.py test app_name`

- a good way to spot untested parts of your application is to check code coverage

- the admin page offers inlines like `StackedInline` and `TabularInline`

- the `DIRS` in `settings.TEMPLATES` entry is a list of filesystem directories to check when loading django templates (search path)

- 