This is the code of [my website](http://ex-mathcompute.herokuapp.com/).
It is a django app. It has the basic features (which at least so far gets the job done for me):

 -- Integrating markdown, mathjax, and code-snippets highlighting for blog posts in django-admin.

 -- Adding images to blog posts in django-admin.

 -- In case you like heroku, it's ready to deploy on heroku (i.e., just set the environment variables, referenced in settings.py, and `git push heroku`. Done). 

** Install **

 -- This project needs Python 2.7.x, PostgreSQL and Redis to be installed on your machine.
 -- Clone the project:
    ```bash 
       git clone https://github.com/mohammad22/fu_proj
    ```
 -- make a virtualenv for the project:
    ```bash 
       mkvirtualenv fun_proj
       workon fun_proj
    ```   
 -- Pip install the required packages:
    `pip install -r requirements.txt`
 -- Run the server and visit `127.0.0.01:8000/blog` in the browser:
    `python manage.py runserver`


