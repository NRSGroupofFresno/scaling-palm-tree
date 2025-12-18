# Contributing to scaling-palm-tree

Thank you for your interest in contributing to the NRS Group of Fresno's scaling-palm-tree project! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the [Issues](https://github.com/NRSGroupofFresno/scaling-palm-tree/issues) section
2. If not, create a new issue with:
   - A clear, descriptive title
   - Detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior

### Making Changes

1. **Fork the repository** (if you don't have write access)

2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/scaling-palm-tree.git
   cd scaling-palm-tree
   ```

3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes** following the project's coding standards

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

6. **Pull the latest changes** from the main repository:
   ```bash
   git checkout main
   git pull origin main
   git checkout feature/your-feature-name
   git merge main
   ```

7. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request** on GitHub

## Pull Request Process

1. Ensure your code follows the project's style guidelines
2. Update documentation if needed
3. Provide a clear description of the changes in your PR
4. Link any related issues
5. Wait for review and address any feedback
6. Once approved, a maintainer will merge your PR

## Commit Message Guidelines

Write clear and meaningful commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep the first line under 50 characters
- Add a detailed description after a blank line if needed

### Examples

Good commit messages:
```
Add user authentication feature
Fix navigation bug on mobile devices
Update README with installation instructions
```

## Git Workflow

For detailed information about Git operations (pull, merge, commit), see our [Git Workflow Guide](GIT_WORKFLOW.md).

### Quick Workflow Summary

1. **Pull** latest changes: `git pull origin main`
2. **Commit** your work: `git commit -m "Your message"`
3. **Merge** branches: `git merge feature-branch`
4. **Push** changes: `git push origin your-branch`

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with the "question" label
- Contact the maintainers

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to scaling-palm-tree!
