# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Code Organization Tool** - a Python script designed to help organize scattered source code across an entire computer. The project is in early development with a minimal starter implementation.

### Project Purpose

The tool will scan, analyze, and organize years of accumulated development projects (scattered across Desktop, Downloads, Documents, external drives, etc.) into a well-structured, clean codebase. It's specifically designed to handle real-world developer "clutter" including:

- Multiple versions of the same project (backups, copies, "final" versions)
- Scattered git repositories with uncommitted/unpushed changes
- IoT/embedded projects with hardcoded credentials
- Old projects with dead dependencies
- Orphaned IDE configurations
- Build artifacts consuming disk space

## Development Commands

This project uses **uv** for Python package management.

### Setup
```bash
# Python version is specified in .python-version (3.12)
# Dependencies are managed in pyproject.toml
```

### Current Status
- Basic project skeleton exists with minimal "Hello World" implementation
- No dependencies defined yet
- Core implementation needs to be built following the design in [code_organizer_prompt.md](code_organizer_prompt.md)

## Architecture

The tool is designed with **two completely isolated phases**:

### Phase 1: Identification & Documentation (Read-Only)
**CRITICAL: Phase 1 makes ZERO filesystem changes**

Split into sub-phases:
- **Phase 1A**: Quick Scan (5-10 minutes) - Fast overview, count projects, identify obvious issues
- **Phase 1B**: Deep Analysis (30-60 minutes) - Comprehensive inventory with:
  - Project classification and metadata
  - Git repository analysis (remotes, branches, uncommitted changes, unpushed commits)
  - Duplicate detection
  - Security scanning (exposed credentials, API keys)
  - Code mining (extracting reusable components)
  - Technology stack analysis
- **Phase 1C**: Interactive Review Mode - Terminal UI to explore results

**Output**: Beautiful, interactive HTML report with charts, filters, and detailed project inventory

### Phase 2: Cleaning & Restructuring (Optional, Prompted)
**CRITICAL: Only runs when explicitly invoked, uses Phase 1 JSON files as input**

Operations (each requiring confirmation):
- **2A**: Quick Wins Cleanup (safe removals: build artifacts, caches)
- **2B**: Extract Reusable Components
- **2C**: Remove Duplicates
- **2D**: Remove Obsolete Projects
- **2E**: Git Repository Cleanup (orphaned .git dirs, nested repos, optimize large repos)
- **2F**: Restructure into Organized Directory
- **2G**: Git Repository Initialization & Remote Setup
- **2H**: Push to Remote (GitHub/GitLab)
- **2I**: Generate Missing Documentation
- **2J**: Generate Final Reports

**Safety Features**:
- Full backup created before ANY changes (including git bundles)
- Rollback script generated
- Dry-run mode available
- Git repos with unpushed commits NEVER deleted without explicit confirmation
- Detailed logging of all operations

### Planned Directory Structure

```
code_organizer/
├── main.py                      # CLI entry point
├── config.py                    # Configuration management
├── phase1_scan/
│   ├── scanner.py               # File system scanning
│   ├── quick_scanner.py         # Phase 1A
│   ├── analyzers.py             # Project analysis
│   ├── duplicate_detector.py
│   ├── security_scanner.py
│   ├── git_analyzer.py          # Git-specific analysis
│   ├── code_miner.py
│   ├── relationship_detector.py
│   └── reporter.py              # HTML report generation
├── phase2_organize/
│   ├── impact_analyzer.py       # Pre-Phase 2 impact summary
│   ├── quick_wins.py
│   ├── code_extractor.py
│   ├── cleaner.py
│   ├── restructurer.py
│   ├── git_manager.py
│   ├── github_manager.py
│   └── doc_generator.py
├── utils/
│   ├── file_utils.py
│   ├── git_utils.py
│   ├── backup.py                # Backup system
│   ├── rollback.py              # Rollback generator
│   └── security_utils.py
├── interactive/
│   ├── review_mode.py           # Phase 1C interactive UI
│   └── prompts.py
└── templates/
    ├── report.html              # HTML report template
    └── readme_template.md
```

## Key Implementation Details

### Technology Detection

The scanner must identify various project types:
- **.NET**: Look for `.sln`, `.csproj`, `.vbproj`, `.fsproj`
- **Python**: Look for `setup.py`, `pyproject.toml`, `requirements.txt`, `*.py`
- **Arduino/Embedded**: Look for `*.ino`, `platformio.ini`
- **ESP32/ESP8266**: esp-idf projects, Arduino framework
- **Web**: `package.json`, `index.html`
- **Docker**: `Dockerfile`, `docker-compose.yml`
- **C/C++**: `Makefile`, `CMakeLists.txt`

### Git Analysis Requirements

Must extract comprehensive git information:
- Repository health (uncommitted changes, unpushed commits, detached HEAD)
- All remotes (GitHub, GitLab, Bitbucket, Azure DevOps, self-hosted)
- Branch information (current, all local/remote)
- Commit history (count, contributors, last commit date)
- Submodules present
- Git LFS usage
- Large files in history (>100MB)
- Orphaned/nested .git directories

### Security Scanning Patterns

Must detect:
- Hardcoded passwords: `password\s*=\s*['"](.+)['"]`
- API keys: `api_key\s*=\s*['"](.+)['"]`
- Private keys: `-----BEGIN PRIVATE KEY-----`
- IoT credentials: WiFi passwords in Arduino sketches, MQTT credentials
- `.env` files tracked in git

### Duplicate Detection Strategy

Multiple detection methods:
- **Name patterns**: `*-backup`, `*-old`, `*-copy`, `Copy of *`, `*-final`
- **Git remotes**: Same remote URL indicates duplicates
- **Content hashing**: Hash files to find exact duplicates
- **Structure comparison**: Similar directory structures

## Dependencies (To Be Installed)

The project will require:
- `rich` - Terminal UI and progress bars
- `click` - CLI framework
- `gitpython` - Git operations (CRITICAL)
- `PyGithub` - GitHub API
- `python-gitlab` - GitLab API
- `jinja2` - HTML templating
- `PyYAML` - Config file parsing
- `pandas` - Data analysis
- `plotly` - Interactive charts
- `questionary` - Interactive prompts
- `networkx` - Project relationship graphs

## Important Constraints

### Safety First
1. **Phase 1 is completely read-only** - never modify filesystem
2. **Phase 2 requires explicit confirmation** at every sub-phase
3. **NEVER delete git repos with unpushed commits** without triple confirmation and backup
4. **Always create full backup** before any Phase 2 operations
5. **Generate rollback scripts** for all destructive operations

### Git Operation Safety
- Verify git bundles are created before deleting any repositories
- Check for uncommitted changes before any git operations
- Test remote connectivity before pushing
- Scan for secrets before pushing to remote
- Never skip git safety checks

### Performance
- Use parallel scanning where possible (multiprocessing)
- Progress tracking for all long operations
- Efficient file hashing (read in chunks)

## Configuration

The tool uses `scan_config.yaml` for configuration (see [code_organizer_prompt.md](code_organizer_prompt.md) for complete example). Key sections:
- `personal_profile` - Developer background, primary languages/platforms
- `scan` - Search paths, exclusions, file patterns
- `git_analysis` - Git scanning settings
- `organization_strategy` - How to organize projects
- `security` - Security scanning patterns
- `git_operations` - GitHub/GitLab settings

## Design Philosophy

### User Control
- User must be in complete control at all times
- Can customize, skip, or abort any operation
- Dry-run mode available for all Phase 2 operations
- Interactive review mode for exploring results

### Real-World Messiness
- Handle edge cases: nested repos, orphaned .git directories, corrupted repos
- Deal with years of accumulated clutter
- Support multiple git hosting platforms
- Handle IoT projects with embedded credentials
- Detect valuable reusable code worth extracting

### Transparency
- Everything logged with timestamps
- Full audit trail of all operations
- Clear before/after comparisons
- Detailed impact summaries before changes

## Testing Approach

When implementing:
- Mock filesystem for testing Phase 1 scanning
- Mock git operations to test without real repos
- Test duplicate detection algorithms thoroughly
- Validate security scanning patterns
- Test rollback functionality
- Integration tests for Phase 2 operations with safety checks

## Current Implementation Status

The repository currently contains:
- Minimal "Hello World" starter in [main.py](main.py)
- Project metadata in [pyproject.toml](pyproject.toml)
- Comprehensive design specification in [code_organizer_prompt.md](code_organizer_prompt.md)

**The core implementation needs to be built according to the design specification.**
