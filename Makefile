PYTHON=python3

clean:
	find $(CURDIR)/src -type f -name "*.py[co]" -delete
	find $(CURDIR)/src -type d -name __pycache__ -delete
