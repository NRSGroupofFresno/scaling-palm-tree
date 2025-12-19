# Contributing to scaling-palm-tree

Thank you for your interest in contributing to the Legal Advocacy & Authorized Rep Services project!

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the issue tracker
2. If not, create a new issue with a clear description
3. Include relevant details such as:
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - System/environment information
   - Screenshots or logs if applicable

### Making Changes

1. **Fork the repository** and create a new branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style and conventions
   - Write clear, concise commit messages
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   make test
   make lint
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request**
   - Provide a clear description of the changes
   - Reference any related issues
   - Ensure all CI checks pass

## Development Setup

```bash
# Clone the repository
git clone https://github.com/NRSGroupofFresno/scaling-palm-tree.git
cd scaling-palm-tree

# Initialize the project
make init

# Install dependencies
make install
```

## Code Style Guidelines

- Write clear, readable code
- Add comments for complex logic
- Follow existing patterns in the codebase
- Keep functions focused and modular
- Use meaningful variable and function names

## Pull Request Process

1. Update documentation for any changed functionality
2. Ensure all tests pass
3. Request review from maintainers
4. Address any feedback from reviewers
5. Once approved, a maintainer will merge your PR

## Code of Conduct

Please note that this project adheres to a Code of Conduct. By participating, you are expected to uphold this code.

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with the `question` label
- Contact the maintainers

Thank you for contributing to making legal advocacy services more accessible!
