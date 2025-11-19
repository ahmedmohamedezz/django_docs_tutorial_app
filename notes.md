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

<!--
    ext.
        - django
        - drf snippets
        - icons
        - pylance
        - python [debugger|environments]
        - python indent
 -->
