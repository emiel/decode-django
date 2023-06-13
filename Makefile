PYTHON=python3

clean:
	find $(CURDIR)/src -type f -name "*.py[co]" -delete
	find $(CURDIR)/src -type d -name __pycache__ -delete

test:
	cd $(CURDIR)/src/decode && ./manage.py test

serve:
	$(CURDIR)/src/decode/manage.py runserver

upgrade-deps:
	pip-compile --upgrade --generate-hashes --resolver=backtracking ./requirements.in
	pip-sync requirements.txt
