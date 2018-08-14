web: gunicorn -w 4 wsgi:app
python mig.py db init
python mig.py db migrate
python mig.py db upgrade