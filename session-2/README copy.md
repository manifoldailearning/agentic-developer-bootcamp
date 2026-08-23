# Git Foundations

This README contains basic Git commands and configurations for reference.

## Command Line Basics

### File System Navigation
- `pwd` - Print Working Directory: Shows the current directory path
- `ls` - List: Shows visible files and directories in current directory
- `ls -a` - List All: Shows both hidden and visible files and directories
- `cd <path_to_directory>` - Change Directory: Navigate to specified directory
- `cd ..` - Change Directory Up: Navigate to parent directory
- `mkdir <directory_name>` - Make Directory: Create a new directory/folder

## Git Commands

### Basic Git Commands
- `git commit -m "message"` - Commit changes with a message
  - Note: Use single dash (-) or double dash (--) for command options

## Git Configuration

### View Configuration
- `git config --global --list` - List all global Git configurations

### Set User Configuration
- `git config --global user.name "your_name"` - Set global Git username
- `git config --global user.email "your_email"` - Set global Git email

Example:
```bash
git config --global user.name "nachiketh"
git config --global user.email "murthy@manifoldailearning.in"
```

## Local Repository Operations

### Repository Initialization
- `.git` - Hidden directory that represents a Git repository
- `git init` - Initialize a new Git repository in the current directory

### File Tracking
- `git status` - Check the status of files in the repository
  - Shows untracked, modified, and staged files

### Staging Files
- `git add <filename>` - Stage a single file for commit
- `git add <filename1> <filename2> <filename3>` - Stage multiple files for commit
- `git add .` - Stage all files in the current directory for commit

### Committing Changes
- `git commit -m "<message>"` - Commit staged changes with a descriptive message
- `git log` - View commit history with details like author, date, and commit messages

Example workflow:
```bash
# Initialize a new repository
git init

# Check status of files
git status

# Stage files for commit
git add example.txt
# or
git add file1.txt file2.txt
# or
git add .

# Commit the changes
git commit -m "Initial commit with example files"

# View commit history
git log
```

## Branching Operations

### Branch Management
- `git branch` - List all branches in the repository
  - Current branch is marked with an asterisk (*)
- `git branch <branch-name>` - Create a new branch
  - Note: This command only creates the branch, it doesn't switch to it

### Switching Branches
- `git switch <branch-name>` - Switch to the specified branch (modern command)
- `git checkout <branch-name>` - Switch to the specified branch (traditional command)
  - Note: `git checkout` has multiple uses, while `git switch` is specifically for changing branches

Example workflow:
```bash
# List all branches
git branch

# Create a new feature branch
git branch feature/new-feature

# Switch to the new branch
git switch feature/new-feature
# or
git checkout feature/new-feature

# Make changes and commit them
git add .
git commit -m "Add new feature implementation"
```

## Merging and Rebasing

### Git Merge
Merging combines the changes from one branch into another, creating a merge commit.

#### Basic Merge Commands
- `git merge <branch-name>` - Merge specified branch into current branch
- `git merge --no-ff <branch-name>` - Create a merge commit even if fast-forward is possible
- `git merge --abort` - Abort the current merge operation

#### Merge Example Workflow
```bash
# Start from main branch
git checkout main

# Merge feature branch into main
git merge feature/new-feature

# If there are conflicts, resolve them and then:
git add .
git commit -m "Merge feature/new-feature into main"
```

### Git Rebase
Rebasing moves or combines a sequence of commits to a new base commit, creating a linear history.

#### Basic Rebase Commands
- `git rebase <branch-name>` - Rebase current branch onto specified branch
- `git rebase -i <commit-hash>` - Interactive rebase to modify commits
- `git rebase --continue` - Continue rebase after resolving conflicts
- `git rebase --abort` - Abort the current rebase operation

#### Rebase Example Workflow
```bash
# Start from feature branch
git checkout feature/new-feature

# Rebase feature branch onto main
git rebase main

# If there are conflicts, resolve them and then:
git add .
git rebase --continue
```

### Merge vs Rebase Comparison

#### When to Use Merge
- When you want to preserve the complete history
- When working on public branches (like main/master)
- When multiple developers are working on the same branch

#### When to Use Rebase
- When you want a clean, linear project history
- When working on local feature branches
- Before merging a feature branch into main

#### Example Scenarios

1. **Merge Scenario**:
```bash
# On main branch
git checkout main
git merge feature/new-feature
# Creates a merge commit preserving both histories
```

2. **Rebase Scenario**:
```bash
# On feature branch
git checkout feature/new-feature
git rebase main
# Creates a linear history by moving feature commits to the tip of main
```

#### Best Practices
- Never rebase commits that have been pushed to a shared repository
- Use merge for public branches
- Use rebase for local feature branches
- Always test your changes after rebasing
- Keep commits small and focused when planning to rebase

## Remote Repository Operations

### Setting Up Remote Repository
- `git remote -v` - List all remote repositories and their URLs
- `git remote add <name> <url>` - Add a new remote repository
- `git remote remove <name>` - Remove a remote repository
- `git remote rename <old-name> <new-name>` - Rename a remote repository

Example:
```bash
# Add a new remote repository
git remote add origin https://github.com/username/repository.git

# Verify remote repositories
git remote -v
```

### Pushing Changes to Remote
- `git push <remote> <branch>` - Push local branch to remote repository
- `git push -u <remote> <branch>` - Push and set upstream tracking
- `git push --force` - Force push changes (use with caution)
- `git push --tags` - Push all tags to remote

Example workflow:
```bash
# Push main branch to origin
git push origin main

# Push new branch and set upstream tracking
git push -u origin feature/new-feature

# Push all tags
git push --tags
```

### Pulling Changes from Remote
- `git pull <remote> <branch>` - Pull and merge changes from remote
- `git fetch <remote>` - Fetch changes without merging
- `git pull --rebase` - Pull and rebase instead of merge

Example workflow:
```bash
# Pull latest changes from main branch
git pull origin main

# Fetch changes without merging
git fetch origin

# Pull and rebase instead of merge
git pull --rebase origin main
```

### Managing Remote Branches
- `git branch -r` - List remote branches
- `git branch -a` - List all branches (local and remote)
- `git checkout -b <branch> <remote>/<branch>` - Create local branch tracking remote branch
- `git push <remote> --delete <branch>` - Delete remote branch

Example workflow:
```bash
# List all remote branches
git branch -r

# Create local branch tracking remote branch
git checkout -b feature/new-feature origin/feature/new-feature

# Delete remote branch
git push origin --delete old-feature
```

### Common Remote Operations

#### Cloning a Repository
```bash
# Clone a repository
git clone https://github.com/username/repository.git

# Clone specific branch
git clone -b <branch> https://github.com/username/repository.git
```

#### Updating Local Repository
```bash
# Fetch all changes from remote
git fetch --all

# Update local branch with remote changes
git pull origin main

# If there are conflicts, resolve them and then:
git add .
git commit -m "Resolve merge conflicts"
git push origin main
```

#### Best Practices for Remote Operations
- Always pull latest changes before starting new work
- Use meaningful commit messages
- Push changes frequently to avoid large merges
- Use feature branches for new features
- Never force push to shared branches
- Keep your local repository clean and organized
- Use pull requests for code review
- Test changes before pushing to main branch

## GitHub Authentication

### Generating Personal Access Token (PAT)

1. **Access GitHub Settings**:
   - Log in to your GitHub account
   - Click on your profile picture in the top-right corner
   - Select "Settings" from the dropdown menu

2. **Navigate to Developer Settings**:
   - Scroll down to the bottom of the left sidebar
   - Click on "Developer settings"

3. **Create Personal Access Token**:
   - Click on "Personal access tokens" → "Tokens (classic)"
   - Click "Generate new token" → "Generate new token (classic)"
   - Give your token a descriptive name
   - Set expiration date (recommended: 30-90 days)
   - Select required permissions:
     - `content` - Full control of private repositories
     - `workflow` - Update GitHub Action workflows
     - `write:packages` - Upload packages to GitHub Package Registry
     - `delete:packages` - Delete packages from GitHub Package Registry
   - Click "Generate token"

4. **Copy and Store Token**:
   - Copy the generated token immediately
   - Store it securely (GitHub won't show it again)
   - Use it as your password when authenticating with Git

### Using the Token

#### Command Line Authentication
```bash
# When prompted for password, use the token instead
git push origin main

# Configure Git to use token for specific repository
git remote set-url origin https://<token>@github.com/username/repository.git
```

#### Storing Token Securely
```bash
# Store token in Git credential manager
git config --global credential.helper store

# Or use credential manager cache (recommended)
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'  # Cache for 1 hour
```

### Best Practices for Token Security
- Never commit tokens to your repository
- Use environment variables for tokens in scripts
- Regularly rotate tokens (update every 30-90 days)
- Use the minimum required permissions
- Revoke tokens that are no longer needed
- Store tokens in secure password managers
- Use different tokens for different purposes
- Monitor token usage in GitHub security settings

### Troubleshooting Token Issues
- If authentication fails:
  1. Verify token hasn't expired
  2. Check token permissions
  3. Ensure token is being used correctly
  4. Try generating a new token
- If token is compromised:
  1. Immediately revoke the token in GitHub settings
  2. Generate a new token
  3. Update all systems using the old token
