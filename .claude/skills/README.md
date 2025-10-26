# Claude Code Skills

This directory contains reusable skills that Claude Code can reference for common tasks.

## Available Skills

### 📦 GitHub Repository Management
**File:** `github-repo-management.md`

Complete workflow for creating GitHub repositories and managing source control:
- Creating repositories via GitHub API
- Token-based authentication
- Security best practices
- Common git operations
- Troubleshooting guide

**When to use:**
- Creating new GitHub repositories
- Pushing code to GitHub
- Managing source control
- Handling git issues

**User info:**
- GitHub username: molaw
- Token storage: `.github_token`
- Default visibility: Public

## How Skills Work

Skills are markdown files that provide detailed instructions for specific tasks. When you mention a task that matches a skill, Claude Code can reference the skill for:

- Consistent workflows
- Best practices
- Security considerations
- Troubleshooting steps
- User-specific configurations

## Creating New Skills

To create a new skill:

1. Create a markdown file in `.claude/skills/`
2. Use descriptive kebab-case naming: `task-name.md`
3. Include:
   - Clear title and description
   - Step-by-step instructions
   - Code examples
   - Common issues and solutions
   - When to use the skill
4. Update this README with the new skill

## Skill Template

```markdown
# Skill Name

Brief description of what this skill does.

## When to Use This Skill

- Use case 1
- Use case 2

## Prerequisites

- Requirement 1
- Requirement 2

## Step-by-Step Instructions

### Step 1: First Step
[Instructions]

### Step 2: Second Step
[Instructions]

## Common Issues and Solutions

### Issue: [Problem]
**Solution:** [Fix]

## Quick Reference

[Useful commands or snippets]
```

## Recommended Skills to Create

Future skills that would be useful:

- **Python Project Setup** - Virtual environments, dependencies, testing
- **Documentation Generation** - README templates, API docs, docstrings
- **Testing & CI/CD** - Pytest setup, GitHub Actions, coverage
- **Code Review** - Review checklist, best practices
- **Deployment** - Publishing to PyPI, Docker containers
- **Database Operations** - Migrations, backups, queries
- **API Development** - REST API patterns, authentication
- **Error Handling** - Logging, debugging, monitoring

## Notes

- Skills are project-specific but can reference user preferences
- Keep skills focused on one task or workflow
- Include both "happy path" and error handling
- Update skills as you learn better approaches
- Skills can reference each other
