release: python manage.py makemigrations && python manage.py migrate
web: gunicorn roastin_coffee.wsgi:application