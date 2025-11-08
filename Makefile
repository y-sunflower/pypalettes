.PHONY: all

coverage:
	uv run coverage run --source=pypalettes -m pytest
	uv run coverage report -m
	uv run coverage xml
	uv run genbadge coverage -i coverage.xml
	rm coverage.xml

preview:
	uv run mkdocs serve

test:
	uv run pytest
