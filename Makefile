runserver:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations $(app)

migrate:
	python3 manage.py migrate