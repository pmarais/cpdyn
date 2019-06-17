# Django Vue ATM

## Quickstart

1. Clone this Repo:
    ```
    git clone git@github.com:pmarais/cpdyn.git
    ```

2. Install pipenv:
    ```
    brew install pipenv
    ```

0. Activate virtual environment and install dev dependencies 
    ```
    pipenv install --dev && pipenv shell
    ```

0. Run server 
    ```
    ./manage.py runserver
    ```

0. Access ATM on [http://localhost:8000/](http://localhost:8000/)

## Get Dev Env Up & Running

1. Clone this Repo:
    ```
    git clone git@github.com:pmarais/cpdyn.git
    ```

2. Install pipenv:
    ```
    brew install pipenv
    ```

0. Activate virtual environment and install dev dependencies 
    ```
    pipenv install --dev && pipenv shell
    ```

1. Update Node (https://nodesource.com/blog/installing-node-js-tutorial-using-nvm-on-mac-os-x-and-ubuntu/):
    ```
    nvm install node
    nvm use node
    ```

0. Migrate `./manage.py migrate`

0. Run `import.R` R-script that will import that data into the SQLite DB, via the Django API. This requires installations of `Lubridate` & `dplyr` & `httr`

0. Build frontend assets `yarn build`

0. Run server 
    ```
    ./manage.py runserver
    ```

0. Access ATM on [http://localhost:8000/](http://localhost:8000/)

-------------

This is a cloned and heavily hacked-together version of [https://github.com/gtalarico/django-vue-template](https://github.com/gtalarico/django-vue-template)