release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn otter_hockey.wsgi:application