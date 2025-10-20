# Contributing to Strands Telegram

Thank you for your interest in contributing to the Strands Telegram tool! This document provides guidelines and information about contributing to this project.

## 🚀 Getting Started

### Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/strands-agents/strands-telegram.git
   cd strands-telegram
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev,test]"
   ```

4. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

### Development Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and test:**
   ```bash
   # Run tests
   make test
   
   # Run linting
   make lint
   
   # Run formatting
   make format
   ```

3. **Commit and push:**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request**

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=strands_telegram

# Run specific test file
pytest tests/test_telegram_tool.py

# Run with verbose output
pytest -v
```

### Writing Tests

- Write tests for all new functionality
- Follow the existing test patterns in `tests/`
- Use descriptive test names
- Mock external API calls using `responses` library
- Aim for high test coverage (>80%)

### Test Structure

```python
import pytest
import responses
from strands_telegram import telegram

class TestTelegramFeature:
    def setup_method(self):
        """Set up test fixtures."""
        pass
    
    @responses.activate
    def test_feature_success(self):
        """Test successful feature operation."""
        # Mock API response
        responses.add(...)
        
        # Test the feature
        result = telegram(...)
        
        # Assert results
        assert result["status"] == "success"
```

## 🏗️ Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

### Style Guidelines

1. **Code Formatting:**
   ```bash
   black src tests
   isort src tests
   ```

2. **Type Hints:**
   - Use type hints for all function parameters and return values
   - Import types from `typing` module when needed

3. **Docstrings:**
   - Use Google-style docstrings
   - Document all public functions and classes
   - Include examples when helpful

```python
def example_function(param: str, optional_param: int = 10) -> Dict[str, Any]:
    """Brief description of the function.

    Args:
        param: Description of the parameter
        optional_param: Description with default value

    Returns:
        Dict containing the result with status and content

    Raises:
        ValueError: When param is invalid

    Example:
        >>> result = example_function("test")
        >>> print(result["status"])
        success
    """
    pass
```

## 📝 Commit Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
feat: add support for inline keyboards
fix: handle network timeout errors properly
docs: update README with new examples
test: add tests for message editing
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Clear description** of the issue
2. **Steps to reproduce** the problem
3. **Expected vs actual behavior**
4. **Environment details** (Python version, OS, etc.)
5. **Code examples** if applicable

Use the bug report template when creating issues.

## 💡 Feature Requests

For feature requests:

1. **Describe the use case** and motivation
2. **Provide examples** of how it would be used
3. **Consider backward compatibility**
4. **Check existing issues** to avoid duplicates

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated (if applicable)
- [ ] Commit messages follow convention

### PR Description

Include in your PR description:

1. **Summary** of changes
2. **Motivation** for the changes
3. **Testing** performed
4. **Breaking changes** (if any)
5. **Related issues** (if applicable)

## 🏆 Recognition

Contributors will be recognized in:

- README.md contributors section
- CHANGELOG.md for significant contributions
- GitHub releases notes

## 📞 Getting Help

- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discord**: Join the Strands Agents Discord community

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to Strands Telegram! 🚀