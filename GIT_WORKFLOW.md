# Git Workflow Guide: Pull, Merge, and Commit

This guide explains the essential Git operations for collaborating on the scaling-palm-tree repository.

## Table of Contents
- [Getting Started](#getting-started)
- [Commit Changes](#commit-changes)
- [Pull Changes](#pull-changes)
- [Merge Changes](#merge-changes)
- [Common Workflows](#common-workflows)
- [Best Practices](#best-practices)

## Getting Started

Before you begin, ensure you have Git installed and have cloned the repository:

```bash
git clone https://github.com/NRSGroupofFresno/scaling-palm-tree.git
cd scaling-palm-tree
```

## Commit Changes

Committing saves your changes to the local repository.

### Basic Commit Workflow

1. **Check the status** of your working directory:
   ```bash
   git status
   ```

2. **Stage files** you want to commit:
   ```bash
   # Stage specific files
   git add filename.txt
   
   # Stage all changes
   git add .
   ```

3. **Commit** your staged changes with a descriptive message:
   ```bash
   git commit -m "Your descriptive commit message"
   ```

### Commit Best Practices

- Write clear, concise commit messages
- Use present tense ("Add feature" not "Added feature")
- Keep commits focused on a single purpose
- Review changes before committing:
  ```bash
  git diff
  ```

## Pull Changes

Pulling fetches and integrates changes from a remote repository.

### Basic Pull

```bash
# Pull changes from the current branch
git pull

# Pull from a specific remote and branch
git pull origin main
```

### Pull with Rebase

To maintain a cleaner history, you can rebase while pulling:

```bash
git pull --rebase origin main
```

### Handle Pull Conflicts

If there are conflicts during a pull:

1. Git will mark the conflicted files
2. Open the files and resolve conflicts manually
3. Stage the resolved files:
   ```bash
   git add resolved-file.txt
   ```
4. Complete the merge:
   ```bash
   git commit
   ```

## Merge Changes

Merging combines changes from different branches.

### Merging a Branch

1. **Switch to the target branch** (the branch you want to merge into):
   ```bash
   git checkout main
   ```

2. **Merge the source branch**:
   ```bash
   git merge feature-branch
   ```

### Merge Strategies

- **Fast-forward merge** (default when possible):
  ```bash
  git merge feature-branch
  ```

- **No fast-forward merge** (creates a merge commit):
  ```bash
  git merge --no-ff feature-branch
  ```

- **Squash merge** (combines all commits into one):
  ```bash
  git merge --squash feature-branch
  git commit -m "Merge feature-branch"
  ```

### Resolving Merge Conflicts

When conflicts occur during a merge:

1. **Identify conflicted files**:
   ```bash
   git status
   ```

2. **Open and edit** conflicted files (look for `<<<<<<<`, `=======`, `>>>>>>>` markers)

3. **Stage resolved files**:
   ```bash
   git add resolved-file.txt
   ```

4. **Complete the merge**:
   ```bash
   git commit
   ```

5. **Abort a merge** if needed:
   ```bash
   git merge --abort
   ```

## Common Workflows

### Feature Branch Workflow

1. Create a new feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```

2. Make changes and commit:
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

3. Pull latest changes from main:
   ```bash
   git checkout main
   git pull origin main
   ```

4. Merge feature branch:
   ```bash
   git merge feature/new-feature
   ```

5. Push changes:
   ```bash
   git push origin main
   ```

### Pull Request Workflow

1. Create and switch to a feature branch
2. Make changes and commit
3. Push your branch:
   ```bash
   git push origin feature/new-feature
   ```
4. Create a Pull Request on GitHub
5. After review and approval, merge via GitHub interface

### Sync Your Fork

If you're working with a forked repository:

1. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/NRSGroupofFresno/scaling-palm-tree.git
   ```

2. Fetch upstream changes:
   ```bash
   git fetch upstream
   ```

3. Merge upstream changes:
   ```bash
   git checkout main
   git merge upstream/main
   ```

4. Push to your fork:
   ```bash
   git push origin main
   ```

## Best Practices

### Before Committing
- Review your changes: `git diff`
- Test your code
- Write meaningful commit messages
- Keep commits atomic and focused

### Before Pulling
- Commit or stash your local changes
- Know which branch you're on: `git branch`
- Consider using `git fetch` first to preview changes

### Before Merging
- Ensure your working directory is clean
- Pull the latest changes from both branches
- Review the changes that will be merged: `git diff main..feature-branch`
- Communicate with your team about significant merges

### General Tips
- Pull frequently to stay up-to-date
- Commit often with meaningful messages
- Use branches for new features or fixes
- Never force push to shared branches
- Use `.gitignore` to exclude unnecessary files

## Quick Reference

```bash
# Check status
git status

# Stage and commit
git add .
git commit -m "Message"

# Pull latest changes
git pull origin main

# Create and switch to new branch
git checkout -b new-branch

# Merge branch
git checkout main
git merge feature-branch

# Push changes
git push origin main

# View commit history
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard local changes
git checkout -- filename.txt
```

## Getting Help

- View Git documentation: `git help <command>`
- View short help: `git <command> --help`
- Online resources: [Git Documentation](https://git-scm.com/doc)

---

For questions specific to this project, please open an issue on GitHub.
