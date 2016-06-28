This is the code of [my website](http://ex-mathcompute.herokuapp.com/).
It is a django app. It has the basic features for a tech blog: 

- Integrating markdown, mathjax, and code-snippets highlighting for blog posts in django-admin.

- Facilitate adding and storing images to the posts in django-admin.

- In case you like heroku, ready to deploy on heroku (i.e., just set the environment variables, referenced in settings.py, and `git push heroku`. Done). 

#### Install 

- This project needs Python 2.7.x, and a PostgreSQL and Redis to be installed on your machine (or to have access to such an environment).
 
- Clone the project:
```shell 
git clone https://github.com/mohammad22/fun_proj
```
 
- make a virtualenv for the project:
```bash 
mkvirtualenv fun_proj
workon fun_proj
```   
 
- Pip install the required packages:
```bash
pip install -r requirements.txt
```
 
- Run the server and visit `127.0.0.01:8000/blog` in the browser:
```bash 
python manage.py runserver
```
- Create a `local_settings.py` in `fun_proj/fun_proj` with the following content:

```python
from settings import BASE_DIR, SITE_ROOT
import os

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USEER': #your name,
        'PASSWORD': # ceredentials of yur database,
        'HOST': # host of your postgres,
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': # host of your redis ,
    },
}    
            
SECRET_KEY = ## create your own secret_key for this project 
```

