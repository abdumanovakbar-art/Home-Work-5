jazzmin:
	pip install -U django-jazzmin


app:
	python manage.py startapp apps

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


dj:
	 python manage.py runserver