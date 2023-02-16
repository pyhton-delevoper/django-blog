run:
	poetry run python manage.py runserver

lint:
	poetry run flake8 hexlet_django_blog

shell:
	poetry run python manage.py shell