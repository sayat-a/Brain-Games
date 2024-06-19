install:
	poetry install

brain-games:
	poetry run brain-games
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl --break-system-packages
	
lint:
	poetry run flake8 brain_games
	
brain-even:
	poetry run brain-even
	
brain-gcd:
	poetry run brain-gcd
	
brain-prime:
	poetry run brain-prime
	
brain-calc:
	poetry run brain-calc
	
brain-progression:
	poetry run brain-progression
