.PHONY: help install install-dev test lint format clean build publish docs

help:
	@echo "Available commands:"
	@echo "  install      Install package in current environment"
	@echo "  install-dev  Install package with development dependencies"
	@echo "  test         Run tests with coverage"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black and isort"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build package"
	@echo "  publish      Publish to PyPI"
	@echo "  docs         Generate documentation"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	python -m pytest tests/ -v --cov=strands_telegram --cov-report=term-missing --cov-report=html

lint:
	flake8 src/ tests/
	mypy src/strands_telegram/
	black --check src/ tests/
	isort --check-only src/ tests/

format:
	black src/ tests/
	isort src/ tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

publish: build
	python -m twine upload dist/*

docs:
	@echo "Documentation is in README.md"
	@echo "For online docs, see: https://github.com/strands-agents/strands-telegram"

# Development workflow
dev-setup: install-dev
	pre-commit install

dev-test: format lint test

dev-clean: clean
	pip uninstall -y strands-telegram

# CI/CD helpers
ci-test:
	python -m pytest tests/ -v --cov=strands_telegram --cov-report=xml

ci-build: clean build