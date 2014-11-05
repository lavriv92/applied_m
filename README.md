Example django project for web seminars
---------------------------------------

1. Installing

install virtualenvwrapper 

http://virtualenvwrapper.readthedocs.org/en/latest/

2. clone project
  
  git clone https://github.com/lavriv92/applied_m.git

3. make virtualenv

  mkvirtualenv django-example
  workon django-example
  cd applied_m

4. Installing django
  pip install -r requirements.txt

5. Synchronize database

  ./manage.py syncdb

6. Run
  ./manage.py runserver

  

