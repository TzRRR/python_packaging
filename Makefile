install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

extract:
	airline_cli extract

transform_load: 
	airline_cli transform_load

query:
	airline_cli query "SELECT * FROM airlineDB1" 

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 
		
all: install lint test format deploy
