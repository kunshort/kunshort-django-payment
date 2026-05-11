.PHONY: test build publish clean

test:
	python -m pytest src/ -v

build: clean
	python -m build

publish: build
	source .env && python -m twine upload dist/*

clean:
	rm -rf dist/ build/ *.egg-info src/*.egg-info
