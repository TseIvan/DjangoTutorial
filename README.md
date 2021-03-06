
# Basic Django Homepage Tutorial

CMPUT 401 Hackathon Fall 2019 Semester && Winter 2020 Semester

# Compiling
  cd to folder that contains manage.py:
  `python3 manage.py createsuperuser` => input username and password you will use to log into admin pages
  
  `python3 manage.py runserver` => navigate to 127.0.0.1:8000 or localhost:8000
  
  if you get error object not found then navigate to admin page by going to 127.0.0.1:8000/admin or localhost:8000/admin and sign-in then create object. Navigate back to website and you will see button and text.

Slides for Google Drive: https://docs.google.com/presentation/d/1307cdHyD-2o8MMwxNkpjVfLaFVp8VZMdcZbNjNATtOA/edit?usp=sharing

# Running in background:
  `nohup python3 manage.py runserver &` => runs in background it will show process number on screen eg: 2773
  
  `kill 2773` => To terminate the process so it no longer runs 
  
  If you forget then type `ps` and find the process that is `python3` and type above command.

# Useful Links to build off of this:

Django Tutorial Youtube:
  https://www.youtube.com/watch?v=UmljXZIypDc
  
Django Tutorial Text (Highly Recommended):
  https://tutorial.djangogirls.org/en/django_start_project/

Django Models:
  https://docs.djangoproject.com/en/2.2/topics/db/models/

Django Class based views:
  https://docs.djangoproject.com/en/2.2/topics/class-based-views/

Django POST Request (Sending information from Front-end to Back-end):
  https://www.youtube.com/watch?v=KRanyK02uO8

Django RESTful API:
  https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/

# Credits
Made by Marissa Snihur & Ivan Tse
