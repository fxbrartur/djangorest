# Django REST Application

Django REST API that I use as a "model/template" for beginning freelance store/ecommerce projects.

## Prerequisites

```
Python 3.8>
Pip
Docker && docker-compose

```

## Quickstart

1. Clone this project

   ```shell
   git clone git@github.com:fxbrartur/djangorest.git
   ```

2. Install dependencies:

   ```shell
   cd djangorest
   pip install -r requirements.txt
   ```

3. Run local dev server:

   ```shell
   python manage.py migrate
   python manage.py runserver
   ```
   
4. Run docker dev server environment:

   ```shell
   docker-compose up -d --build 
   docker-compose exec web python manage.py migrate
   ```

5. Run tests inside of docker:

   ```shell
   docker-compose exec web python manage.py test
   ```
