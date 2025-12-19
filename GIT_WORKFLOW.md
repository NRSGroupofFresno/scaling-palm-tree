# Git Workflow Guide: Merge, Commit, and Pull

## Overview
This guide explains how to work with Git for collaborative development, covering the essential operations: merge, commit, and pull.

## Basic Workflow

### 1. Commit Your Changes
Before merging or pulling, always commit your local changes:

```bash
# Check status of your working directory
git status

# Add files to staging area
git add <filename>
# Or add all changes
git add .

# Commit changes with a descriptive message
git commit -m "Description of changes"
```

### 2. Pull Latest Changes
Pull the latest changes from the remote repository:

```bash
# Pull changes from the current branch
git pull origin <branch-name>

# Or pull with rebase to maintain linear history
git pull --rebase origin <branch-name>
```

### 3. Merge Branches
When you need to integrate changes from one branch into another:

```bash
# Switch to the branch you want to merge INTO
git checkout main

# Merge another branch into the current branch
git merge <feature-branch>

# If conflicts occur, resolve them and then:
git add <resolved-files>
git commit -m "Merge <feature-branch> into main"
```

## Complete Workflow Example

### Scenario: Update your feature branch and merge to main

```bash
# 1. Ensure you're on your feature branch
git checkout feature-branch

# 2. Commit any pending changes
git add .
git commit -m "Complete feature implementation"

# 3. Pull latest changes from remote
git pull origin feature-branch

# 4. Switch to main branch
git checkout main

# 5. Pull latest main branch changes
git pull origin main

# 6. Merge your feature branch
git merge feature-branch

# 7. Push the merged changes
git push origin main
```

## Handling Merge Conflicts

When merge conflicts occur:

```bash
# 1. Git will mark conflicting files
# 2. Open conflicting files and look for conflict markers:
#    <<<<<<< HEAD
#    your changes
#    =======
#    incoming changes
#    >>>>>>> branch-name

# 3. Manually resolve conflicts by editing the files
# 4. Remove conflict markers
# 5. Add resolved files
git add <resolved-file>

# 6. Complete the merge
git commit -m "Resolved merge conflicts"

# 7. Push changes
git push
```

## Best Practices

1. **Commit Often**: Make small, logical commits with clear messages
2. **Pull Before Push**: Always pull latest changes before pushing
3. **Review Before Merge**: Review changes before merging branches
4. **Keep Branches Updated**: Regularly merge main into feature branches
5. **Test After Merge**: Always test after merging to ensure nothing breaks
6. **Use Descriptive Commit Messages**: Help others understand your changes

## Common Commands Reference

```bash
# View commit history
git log --oneline

# View branch structure
git branch -a

# View changes
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard local changes
git checkout -- <filename>

# Update all remote branches
git fetch --all
```

## Pull Request Workflow

For team collaboration:

1. Create a feature branch
2. Make and commit changes
3. Push to remote repository
4. Create a Pull Request (PR)
5. Review and discuss changes
6. Merge PR after approval
7. Delete feature branch after merge

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
