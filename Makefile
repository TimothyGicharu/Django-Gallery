runserver:
	./manage.py runserver

migrations:
	./manage.py makemigrations $(app)

migrate:
	./manage.py migrate

start:
	django-admin startapp $(name)