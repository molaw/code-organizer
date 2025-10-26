# GitHub Repository Management Skill

This skill provides complete instructions for creating GitHub repositories and managing source control for user molaw.

## User Information

- **GitHub Username:** molaw
- **GitHub Profile:** https://github.com/molaw
- **Token Storage:** `.github_token` in project root (always add to .gitignore)

## Prerequisites Check

Before starting any GitHub operations:
1. Check if `.github_token` exists in project root
2. If token file doesn't exist, ask user for their GitHub Personal Access Token
3. Create `.github_token` file with the token
4. Ensure `.github_token` is in `.gitignore`

## Step-by-Step GitHub Repository Creation

### Step 1: Initialize Local Git Repository

```bash
# Check if already a git repo
if [ ! -d .git ]; then
    git init
fi

# Set branch name to main
git branch -M main
```

### Step 2: Create Comprehensive .gitignore

Ensure .gitignore includes:
```
# Python
__pycache__/
*.py[oc]
build/
dist/
*.egg-info
.venv
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
CodeOrganization_Logs/
CodeOrganization_Backups/

# Test outputs
.pytest_cache/
.coverage
htmlcov/

# Secrets - CRITICAL
.github_token
*.token
.env
.env.local
```

### Step 3: Stage and Commit Files

```bash
# Stage all files
git add .

# Create initial commit with detailed message
git commit -m "$(cat <<'EOF'
Initial commit: [Brief description]

[Detailed description of what's included]

Features implemented:
- Feature 1
- Feature 2
- Feature 3

Technology stack:
- Technology 1
- Technology 2

Next steps:
- Future feature 1
- Future feature 2

Generated with Claude Code (claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

### Step 4: Create GitHub Repository via API

```bash
# Read token from file
TOKEN=$(cat .github_token)

# Create repository
curl -X POST \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{
    "name":"repository-name",
    "description":"Repository description",
    "private":false,
    "has_issues":true,
    "has_projects":true,
    "has_wiki":true
  }'
```

**Note:** Repository name should be kebab-case (lowercase with hyphens)

### Step 5: Add Remote and Push

```bash
# Read token for authenticated URL
TOKEN=$(cat .github_token)

# Add remote with token authentication
git remote add origin https://$TOKEN@github.com/molaw/repository-name.git

# Or if remote already exists, update it
git remote set-url origin https://$TOKEN@github.com/molaw/repository-name.git

# Push to GitHub
git push -u origin main
```

### Step 6: Verify Push Success

```bash
# Check repository exists
curl -s https://api.github.com/repos/molaw/repository-name | grep '"name"'

# Or check branch status
git status
```

## Common Follow-Up Operations

### Commit and Push Changes

```bash
# Check what changed
git status

# Stage changes
git add .

# Or stage specific files
git add path/to/file1 path/to/file2

# Commit with message
git commit -m "Brief description

Detailed explanation of changes:
- Change 1
- Change 2
- Change 3"

# Push to GitHub
git push
```

### Amend Last Commit (Before Push)

```bash
# Make additional changes
git add .

# Amend previous commit
git commit --amend --no-edit

# Force push (only if not yet pushed or no one else has pulled)
git push --force-with-lease
```

### Handle Push Protection (Secret Detected)

If GitHub detects a secret:

1. **Remove the secret from the file**
2. **Add the file pattern to .gitignore**
3. **Amend the commit:**
   ```bash
   git add .gitignore
   git add path/to/cleaned/file
   git commit --amend --no-edit
   ```
4. **Force push:**
   ```bash
   git push --force-with-lease
   ```

### Create Feature Branch

```bash
# Create and switch to new branch
git checkout -b feature/feature-name

# Make changes and commit
git add .
git commit -m "Implement feature"

# Push feature branch
git push -u origin feature/feature-name

# Switch back to main
git checkout main

# Merge feature (when ready)
git merge feature/feature-name
git push
```

## Security Best Practices

### Always Protect Secrets

1. **Never commit tokens** - Add to .gitignore
2. **Check before push** - Review `git diff --cached`
3. **Use token files** - Store in `.github_token`, `.env`, etc.
4. **Clean commit history** - Use `--amend` if secret detected before push
5. **Rotate tokens** - If accidentally exposed, revoke and create new

### Token Management

```bash
# Store token securely
echo "ghp_xxxxxxxxxxxxx" > .github_token

# Ensure in .gitignore
echo ".github_token" >> .gitignore

# Use in scripts
TOKEN=$(cat .github_token)
```

## Common Issues and Solutions

### Issue: "Repository not found"
**Solution:** Repository hasn't been created on GitHub yet
```bash
# Create via API first (see Step 4)
```

### Issue: "Push declined due to repository rule violations"
**Solution:** Secret detected in commit
```bash
# Remove secret, amend commit, force push (see "Handle Push Protection")
```

### Issue: "Authentication failed"
**Solution:** Token expired or incorrect
```bash
# Get new token from https://github.com/settings/tokens
# Update .github_token file
echo "ghp_newtoken" > .github_token
```

### Issue: "Failed to push some refs"
**Solution:** Remote has changes you don't have
```bash
# Pull changes first
git pull --rebase
git push
```

### Issue: LF/CRLF warnings on Windows
**Solution:** Normal behavior, can be ignored or configured
```bash
# Configure git to handle line endings (optional)
git config --global core.autocrlf true
```

## Complete Workflow Example

Here's a complete example for a new Python project:

```bash
# 1. Initialize repository
git init
git branch -M main

# 2. Create .gitignore (include secrets patterns)
cat > .gitignore << 'EOF'
__pycache__/
*.py[oc]
.venv/
.github_token
*.token
.env
EOF

# 3. Save token
echo "ghp_xxxxxxxxxxxxx" > .github_token

# 4. Stage and commit
git add .
git commit -m "Initial commit: Project setup

Includes:
- Project structure
- Dependencies configured
- Documentation

Built with Claude Code"

# 5. Create GitHub repo
TOKEN=$(cat .github_token)
curl -X POST \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"my-project","description":"My awesome project","private":false}'

# 6. Add remote and push
git remote add origin https://$TOKEN@github.com/molaw/my-project.git
git push -u origin main

# 7. Verify
echo "Repository created: https://github.com/molaw/my-project"
```

## Git Commit Message Format

Use this format for professional commits:

```
Brief description (50 chars or less)

Detailed explanation (wrap at 72 characters):
- What changed
- Why it changed
- Any important notes

Technical details:
- Implementation specifics
- Dependencies added/removed
- Breaking changes

Generated with Claude Code (claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Repository Naming Conventions

- Use **kebab-case**: `my-project-name`
- Be **descriptive**: `code-organizer` not `tool`
- Keep it **short**: 2-4 words maximum
- Use **nouns**: `data-analyzer` not `analyze-data`
- Avoid **redundancy**: `js-library` not `javascript-library-js`

## Quick Reference Commands

```bash
# Status
git status                    # Check what changed
git log --oneline            # View commit history
git diff                     # See unstaged changes

# Basic workflow
git add .                    # Stage all changes
git commit -m "message"      # Commit changes
git push                     # Push to GitHub

# Branches
git checkout -b feature/x    # Create new branch
git checkout main            # Switch to main
git merge feature/x          # Merge branch

# Undo
git checkout -- file         # Discard changes to file
git reset HEAD file          # Unstage file
git commit --amend           # Modify last commit

# Remote
git remote -v                # Show remotes
git pull                     # Get latest changes
git push --force-with-lease  # Force push safely
```

## Integration with Claude Code Workflows

When Claude Code needs to create a GitHub repository:

1. **Check for token:** Look for `.github_token` file
2. **Ask if needed:** If no token, ask user to provide one
3. **Follow security:** Always add token files to .gitignore
4. **Use API:** Create repo via GitHub API (not gh CLI)
5. **Verify success:** Check repository was created
6. **Push code:** Use authenticated HTTPS URL
7. **Confirm:** Show user the repository URL

## Token Permissions Required

When asking user for a Personal Access Token, it should have:

- ✅ `repo` - Full control of private repositories
- ✅ `workflow` - Update GitHub Actions workflows (optional)

Generate at: https://github.com/settings/tokens

## After Repository Creation

Tell the user:

1. **Repository URL:** https://github.com/molaw/repository-name
2. **Clone command:** `git clone https://github.com/molaw/repository-name.git`
3. **Next steps:** What features to implement next
4. **Security notes:** Confirm secrets are protected

## This Skill Should Be Used When:

- User asks to "create a GitHub repository"
- User asks to "push to GitHub"
- User asks "how do I push this code"
- User mentions "source control" or "git"
- Starting a new project that needs version control
- User provides a GitHub Personal Access Token

## Remember:

- **Username:** molaw
- **Token storage:** `.github_token` (always .gitignore)
- **Default visibility:** Public (unless user specifies private)
- **Authentication:** Token-based HTTPS URLs
- **Branch name:** main (not master)
- **Commit style:** Detailed with "Generated with Claude Code"
