# Code Organizer - Complete Prompt for Claude Code

## Overview

I need you to create a Python script that will help me organize all source code on my computer. This should be built as a multi-phase tool with completely isolated functions. I've been developing on this computer for years and have code scattered everywhere - I need to consolidate and organize it all.

---

## PHASE 1: IDENTIFICATION & DOCUMENTATION (Read-Only)

This phase ONLY scans and documents - it makes ZERO changes to the filesystem.

Phase 1 is split into sub-phases for efficiency:

### PHASE 1A: Quick Scan (5-10 minutes)

Fast overview to give immediate insights:
- Count projects by type
- Identify obvious duplicates (same name, same git remote)
- Find "quick wins" (empty folders, huge build artifacts, node_modules)
- Security red flags (exposed credentials)
- Estimate cleanup potential (space that can be freed)
- Generate quick summary report

### PHASE 1B: Deep Analysis (30-60 minutes)

Comprehensive inventory of everything:

#### Scanning Requirements

Search entire computer with special focus on common developer clutter locations:

**High Priority Locations** (where code typically accumulates):
```
- ~/Desktop
- ~/Downloads
- ~/Documents/Projects
- ~/Documents/GitHub
- ~/Source
- ~/dev
- ~/code
- ~/workspace
- C:/Users/{user}/Source/Repos (Visual Studio default on Windows)
- Any external drives or USB backups
```

**File Types & Patterns to Find**:

- .NET solutions (.sln) and projects (.csproj, .vbproj, .fsproj)
- Python projects (look for setup.py, pyproject.toml, requirements.txt, or directories with .py files)
- Arduino/embedded projects (.ino files, platformio.ini)
- ESP32/ESP8266 projects (esp-idf, Arduino framework)
- SQL files and scripts (.sql)
- Bash scripts (.sh)
- YAML configuration files (docker-compose.yml, .gitlab-ci.yml, .github/workflows/*.yml, etc.)
- C/C++ projects (Makefile, CMakeLists.txt, .c, .cpp, .h files)
- Web projects (package.json for Node.js projects)

**IDE Configuration Files**:
- VS Code workspaces (.code-workspace)
- VS Code settings folders (.vscode/)
- Cursor IDE configurations (.cursor/, .cursorrules)
- Windsurf IDE configurations (.windsurf/)
- JetBrains IDEs (.idea/)
- Visual Studio settings (.vs/)
- Sublime Text projects (.sublime-project, .sublime-workspace)
- Atom projects (.atom/)
- Eclipse projects (.project, .classpath)

**Docker Related Files**:
- Dockerfile, Dockerfile.*
- docker-compose.yml, docker-compose.*.yml
- .dockerignore
- Kubernetes manifests (*.yaml, *.yml in k8s/ or kubernetes/ directories)
- Helm charts (Chart.yaml, values.yaml)
- Container build scripts
- .env files associated with Docker projects

**SSH Configurations**:
- SSH config files (~/.ssh/config and project-specific configs)
- SSH key pairs (*.pub, *.pem - document location only)
- Known_hosts files
- SSH connection scripts
- Remote development configurations
- Vagrant configurations (Vagrantfile)

**Git Files & Repositories**:
- .git directories (repository roots)
- .gitignore files
- .gitattributes files
- .gitmodules (for submodules)
- Git hooks (in .git/hooks/)
- Bare repositories (*.git directories without working tree)
- Git bundles (*.bundle files)
- .gitkeep files
- Orphaned .git directories (repos without code)
- Nested .git directories (submodules or accidentally nested repos)

#### Analysis & Classification

For each discovered item, analyze and document:

**Project Name & Type**: (e.g., "Python Web App", ".NET WPF Application", "ESP32 IoT Project")

**Location**: Full path

**Size**: Total size in MB/GB

**Last Modified**: Date of most recent change

**Activity Level**:
- ACTIVE: Last modified < 6 months ago
- MAINTAINED: 6 months - 2 years
- REFERENCE: 2-5 years (completed/working, might need)
- ARCHIVE: 5+ years old
- STALE: Old with uncommitted changes

**Git Status**: 
- Has git repo? (yes/no)
- Repository size (.git folder size)
- Remote configured? (URL if yes - list all remotes)
- Remote type: (GitHub, GitLab, Bitbucket, Azure DevOps, self-hosted, etc.)
- Uncommitted changes? (count of modified/added/deleted files)
- Untracked files? (count)
- Branch name (current branch)
- All branches (local and remote)
- Stashes present? (count)
- Last commit date
- Total commit count
- Contributors (count and list)
- Submodules present? (list them)
- Git LFS in use? (yes/no)
- Repository health:
  - Very large files in history (>100MB)
  - Accidental commits of sensitive files
  - Uncommitted changes for extended period

**Associated Files**:
- IDE configurations found
- Docker files found
- SSH configs found
- Environment files (.env)
- Git configuration files
- README present? (yes/no)
- Tests present? (yes/no)
- Documentation folder? (yes/no)

**Completeness Score**: (0-100% based on):
- Has main entry point (20 points)
- Has documentation/README (15 points)
- Has dependencies file (15 points)
- Has git history (15 points)
- Number of commits (10 points: 0 for <10, 5 for 10-50, 10 for 50+)
- Has tests (10 points)
- Has .gitignore (10 points)
- Has meaningful commit messages (5 points)

**Technology Stack**:
- Primary language(s)
- Frameworks/libraries detected
- Target platform (Windows/Linux/Arduino/ESP32/etc.)
- Dependencies and versions

**Potential Issues**:
- Appears incomplete (low completeness score)
- Contains "test", "temp", "old", "backup", "copy", "final" in path
- No activity in X years
- Orphaned IDE config
- Hardcoded credentials detected
- Private SSH keys in project directory (SECURITY WARNING)
- Docker containers with no associated code

**Git-specific issues**:
- Orphaned .git directory (no source code)
- Nested .git directories (accidental or misconfigured)
- Large .git directory (>500MB)
- No remote configured (local only, no backup)
- Remote URL unreachable or deprecated
- Uncommitted changes for >1 year
- Git repo but no .gitignore
- Sensitive files tracked in git (.env, private keys, etc.)
- Merge conflicts unresolved
- Detached HEAD state
- Has unpushed commits

**IoT/Embedded specific**:
- WiFi passwords in code
- API keys in Arduino sketches
- MQTT credentials hardcoded
- Device serial numbers exposed

**Duplicate Candidates**:
- List other projects with similar names
  - "project" vs "project-backup" vs "project-old" vs "project-final"
  - "Copy of X" folders
- List projects with similar file structure
- List projects with matching content hashes
- List projects with same git remote URL (potential duplicates)
- List bare repos vs working repos of same project
- Confidence score (0-100%)
- Recommendation: KEEP (which one) vs DELETE (which ones)

**Project Relationships**:
- Related projects (frontend + backend)
- Shared libraries/dependencies
- Projects that import each other
- Same project, different platforms (Arduino vs ESP32 version)

**Reusable Components** (Code Mining):
- Custom libraries worth extracting
- Useful utilities/scripts
- Working configuration templates
- Tested deployment scripts
- Code patterns worth keeping
- Well-documented functions/classes

**Dependency Analysis**:
- Using dead technologies? (Python 2.7, .NET Framework 4.0, etc.)
- Deprecated libraries
- Outdated IoT SDKs
- Old Arduino libraries that need updating

**Recommended Action**:
- KEEP & ORGANIZE - Active projects
- ARCHIVE - Old but valuable for reference
- EXTRACT COMPONENTS - Has reusable code, then archive
- DELETE - True garbage
- NEEDS UPDATE - Good project but outdated dependencies
- NEEDS DOCUMENTATION - Missing README

#### Quick Wins Detection

Identify immediately cleanable items with zero risk:

- Empty project folders (0 code files)
- node_modules directories not in active projects
- Build artifacts (bin/, obj/, build/, dist/, target/)
- Python __pycache__ directories
- .vs folders not in active solutions
- Duplicate ZIP/RAR backups of projects
- Temp/cache directories
- Old virtual environments (.venv, venv, env)

Calculate space savings for each category.

### PHASE 1C: Interactive Review Mode

After deep analysis completes, provide an interactive terminal interface:

```
CODE ORGANIZER - Interactive Review
══════════════════════════════════════════════════════════════

📊 Quick Stats:
   Total Projects: 287
   Total Size: 156 GB
   Quick Win Space: 42 GB (can be freed safely)
   Security Issues: 8 (need attention)

🔍 Commands:
   [V] View full report in browser
   [D] Drill into project details
   [F] Filter/search projects
   [C] Compare two projects
   [S] Show duplicates
   [Q] Quick wins (safe cleanup)
   [R] Relationships graph
   [T] Technology timeline
   [M] Mark decisions
   [E] Export subset
   [G] Generate final report & proceed to Phase 2
   [X] Exit without saving

Select command:
```

### Output Format - Interactive HTML Dashboard

Generate a beautiful, filterable, sortable HTML report with:

#### Executive Summary (Top of page)

```
🎯 ORGANIZATION PLAN SUMMARY
═══════════════════════════════════════════════════════════════

CURRENT STATE:
• Total Projects Found: 287
• Total Size: 156.3 GB
• Active Projects (< 6mo): 45
• Maintained (6mo-2yr): 67
• Reference (2-5yr): 89
• Archive (5+ yrs): 58
• Incomplete/Test: 28

CLEANUP POTENTIAL:
• Space in quick wins: 42.1 GB (safe to remove)
• Space in duplicates: 18.7 GB
• Space in obsolete projects: 31.4 GB
• Total recoverable: 92.2 GB (59%)

SECURITY ALERTS:
🔴 8 Critical: Private keys, exposed passwords
🟡 23 Warnings: Hardcoded credentials, no .gitignore

RECOMMENDED ACTIONS:
✓ Keep & Organize: 156 projects → ~/CodeOrganized
📦 Archive: 89 projects → ~/CodeArchive  
🔧 Extract Components: 12 projects (reusable code)
🗑️  Delete: 45 projects (garbage)
📤 Push to GitHub: 23 projects (no remote backup)
```

#### Technology Stack Timeline (Visual)

```
YOUR DEVELOPMENT EVOLUTION
═══════════════════════════════════════════════

2018 ████████░░░░░░░░░░  Arduino C++ (32 projects)
     ███░░░░░░░░░░░░░░░  Python Scripts (8 projects)

2019 ████████████░░░░░░  Arduino C++ (45 projects)
     ██████░░░░░░░░░░░░  Python (18 projects)
     ██░░░░░░░░░░░░░░░░  ESP32 Projects (6 projects)

2020 ██████░░░░░░░░░░░░  Arduino (22 projects)
     ████████████░░░░░░  Python (38 projects)
     ██████░░░░░░░░░░░░  .NET/WPF (14 projects)
     ████░░░░░░░░░░░░░░  ESP32 (11 projects)

2021 ████░░░░░░░░░░░░░░  Arduino (12 projects)
     ██████████████░░░░  Python (42 projects)
     ████████░░░░░░░░░░  .NET/C# (24 projects)
     ██████░░░░░░░░░░░░  Docker Projects (15 projects)
     ████░░░░░░░░░░░░░░  ESP32 (10 projects)

2022-2024 
     ███░░░░░░░░░░░░░░░  Arduino (9 projects)
     ████████████████░░  Python (51 projects)
     ████████████░░░░░░  .NET/C# (35 projects)
     ██████████░░░░░░░░  Docker (28 projects)
     ██████░░░░░░░░░░░░  ESP32/IoT (18 projects)
     ████░░░░░░░░░░░░░░  Full-stack Web (12 projects)

INSIGHTS:
• Peak Arduino development: 2019
• Steady Python growth throughout
• .NET adoption started 2020
• Docker/DevOps focus since 2021
• IoT embedded projects consistent
```

#### Summary Statistics Section

- Total projects found: X
- By type: (pie chart)
  - .NET: X projects
  - Python: X projects
  - Embedded/IoT: X projects
  - Arduino: X projects
  - Docker/DevOps: X projects
  - Scripts: X files
  - Web: X projects
- By activity level: (bar chart)
  - ACTIVE: X
  - MAINTAINED: X
  - REFERENCE: X
  - ARCHIVE: X
- By status:
  - Complete projects: X
  - Incomplete projects: X
  - Has git: X
  - No git: X
  - Has remote: X
  - Local only: X
  - Potential duplicates: X groups
  - Security warnings: X
- Total size: X GB
- Total git repository size: X GB
- Oldest project: (name, date)
- Newest project: (name, date)
- Most active repo: (name, commit count)

#### Quick Wins Section (Expandable)

```
🎁 QUICK WINS - Safe to Remove (Zero Risk)
═══════════════════════════════════════════════

Immediate space savings: 42.1 GB

✓ Empty project folders: 47 folders (12 MB)
  [View List] [Select All] [Remove]

✓ node_modules not in active projects: 12 dirs (8.4 GB)
  ~/old-web-project/node_modules (2.1 GB)
  ~/Downloads/react-app/node_modules (1.8 GB)
  ... (show top 5, expandable)
  [View All] [Select All] [Remove]

✓ Build artifacts: 23 locations (3.2 GB)
  ~/projects/dotnet-app/bin/ (456 MB)
  ~/projects/cpp-project/build/ (892 MB)
  ... (show top 5, expandable)
  [View All] [Select All] [Remove]

✓ Python __pycache__: 156 directories (287 MB)
  [View List] [Select All] [Remove]

✓ .vs folders (Visual Studio): 31 dirs (1.8 GB)
  [View List] [Select All] [Remove]

✓ Old virtual environments: 18 dirs (4.2 GB)
  [View List] [Select All] [Remove]

✓ Duplicate ZIP backups: 8 files (2.1 GB)
  project-backup-v1.zip (456 MB) vs project-backup-v2.zip (461 MB)
  ... (list all)
  [View List] [Select All] [Remove]

[Execute Quick Cleanup] [Export List] [Cancel]
```

#### Skills Inventory / Portfolio Summary

```
🎓 YOUR DEVELOPMENT PORTFOLIO
═══════════════════════════════════════════════

Based on 287 projects analyzed:

LANGUAGES:
• C/C++ (Arduino, ESP32): 98 projects, ~85,000 lines
• C# (.NET, WPF): 73 projects, ~120,000 lines
• Python: 109 projects, ~156,000 lines
• JavaScript/TypeScript: 34 projects, ~42,000 lines
• SQL: 45 files, ~8,000 lines
• Bash/Shell: 67 scripts

FRAMEWORKS & TECHNOLOGIES:
• WPF Desktop Applications
• Arduino Framework
• ESP-IDF (ESP32)
• Flask/Django (Python web)
• Docker & Kubernetes
• React/Node.js

IoT & EMBEDDED:
• ESP32/ESP8266: 47 projects
• Arduino (Various boards): 89 projects
• Raspberry Pi: 12 projects
• Custom PCB projects: 8
• MQTT, WiFi, Bluetooth implementations

SOFTWARE ENGINEERING:
• Desktop Applications (WPF): 35 projects
• Web Applications: 28 projects
• Automation Scripts: 67
• Database Projects: 23
• API Development: 18

DevOps & INFRASTRUCTURE:
• Docker: 28 projects
• Docker Compose: 19 multi-container apps
• CI/CD Pipelines: 12 projects
• Infrastructure as Code: 6 projects

VERSION CONTROL:
• Git repositories: 203
• Total commits: ~12,450
• Unique contributors collaborated with: 15
• Open source contributions: 8 repos

TOTAL OUTPUT:
• ~411,000 lines of code
• 287 projects
• ~6+ years of development
• Active across 8+ technology stacks

[Export as PDF Resume] [Export as JSON] [Copy to Clipboard]
```

#### Security Dashboard

```
🔒 SECURITY ANALYSIS
═══════════════════════════════════════════════

🔴 CRITICAL ISSUES (Immediate Action Required): 8

1. Private SSH keys in project directories:
   ⚠️ ~/projects/iot-device/id_rsa (PRIVATE KEY EXPOSED!)
   ⚠️ ~/old-projects/deploy/server.pem
   → ACTION: Move to ~/.ssh/ and remove from projects

2. Hardcoded passwords in code:
   ⚠️ ~/projects/web-app/config.py - Line 23: password="admin123"
   ⚠️ ~/arduino/esp32-mqtt/esp32-mqtt.ino - Line 45: WiFi password
   → ACTION: Move to environment variables

3. API keys exposed:
   ⚠️ ~/projects/weather-app/api_keys.py (OpenWeather API key)
   ⚠️ ~/esp32/cloud-logger/main.cpp (AWS IoT credentials)
   → ACTION: Use secret management

🟡 WARNINGS (Should Fix): 23

1. WiFi credentials in IoT projects: 12 files
   - ~/arduino/esp8266-sensor/esp8266-sensor.ino
   - ~/esp32-projects/home-automation/config.h
   ... (show all)

2. MQTT broker credentials hardcoded: 6 projects
3. No .gitignore in repos: 18 projects (risk of committing secrets)
4. .env files tracked in git: 8 projects
5. Public keys in unusual locations: 5 files

[Generate Security Report] [Fix Automatically Where Possible] [Export]
```

#### Git Repository Dashboard

```
📚 GIT REPOSITORY ANALYSIS
═══════════════════════════════════════════════

OVERVIEW:
• Total repositories found: 203
• With remotes: 178 (88%)
• Local only (no backup!): 25 (12%)
• Orphaned .git directories: 7
• Nested repositories (issues): 4
• Bare repositories: 2

REPOSITORY HEALTH:
✓ Healthy: 156 repos
⚠️ Needs Attention: 38 repos
🔴 Critical Issues: 9 repos

BREAKDOWN BY HOST:
GitHub: 142 repos
  • Personal account: 89 repos
  • Organizations:
    - mycompany: 34 repos
    - iot-projects: 12 repos
    - opensource-contrib: 7 repos

GitLab: 28 repos
  • Self-hosted (gitlab.company.com): 28 repos

Bitbucket: 5 repos

Local Only (NO REMOTE - RISK OF LOSS): 25 repos
  ⚠️ ~/projects/important-client-work (47 commits, no backup!)
  ⚠️ ~/esp32/production-firmware (156 commits, no backup!)
  ... (list all)
  [Push to GitHub] [Push to GitLab] [Create Remotes]

REPOSITORIES WITH ISSUES:
🔴 Uncommitted changes for >1 year: 12 repos
  ~/old-projects/web-app (uncommitted since 2022-03-15)
  ... (list all)

🔴 Unpushed commits: 8 repos
  ~/projects/mobile-app (23 unpushed commits!)
  ... (list all)

⚠️ No .gitignore: 18 repos
⚠️ Large repos (>500MB): 6 repos
⚠️ Orphaned .git (no code): 7 locations
⚠️ Nested .git (conflicts): 4 locations

ACTIVITY STATS:
• Total commits across all repos: 12,450
• Most active repo: iot-platform (892 commits)
• Largest repo: machine-learning-project (2.3 GB)
• Oldest repo: first-arduino-project (2018-02-14)
• Most contributors: company-backend (12 people)

SUBMODULES IN USE: 8 repos
• web-platform (3 submodules)
• monorepo-project (5 submodules)
```

#### Project Inventory Table (sortable, filterable)

Columns:
- [Checkbox] for Phase 2 selection
- Project Name
- Type
- Activity Level (color-coded badges)
- Path (clickable to open in file manager)
- Size
- Last Modified
- Completeness Score (color-coded progress bar: green >80%, yellow 50-80%, red <50%)
- Git Status (detailed icons):
  - ✓ with remote (show host icon: GitHub/GitLab/etc.)
  - ✓ local only
  - ⚠ uncommitted changes (count)
  - ⚠ unpushed commits (count)
  - ⚠ no remote
  - ✗ no git
- Git Details (expandable):
  - Remote URL(s)
  - Branch: name
  - Commits: count
  - Last commit: date
  - Contributors: count
  - Uncommitted: count files
  - Untracked: count files
  - Unpushed: count commits
- IDE Configs (icons for VS Code, Cursor, etc.)
- Docker (icon if has Dockerfile/compose)
- Has Tests (✓/✗)
- Has README (✓/✗)
- Issues (expandable list with icons)
- Recommended Action (badge: KEEP/ARCHIVE/DELETE/EXTRACT)
- Reusable Components (if any detected)
- Related Projects (links to related)

#### Filter Panel (Sidebar)

```
FILTERS:
□ Show only ACTIVE
□ Show only needs action
□ Show only with git issues
□ Show only security issues
□ Show only duplicates
□ Show only incomplete
□ Show only no remote

BY TYPE:
□ .NET (73)
□ Python (109)
□ Arduino (89)
□ ESP32 (47)
□ Docker (28)
□ Web (34)

BY SIZE:
□ > 1GB (12)
□ 100MB - 1GB (45)
□ < 100MB (230)

BY ACTIVITY:
□ Active (45)
□ Maintained (67)
□ Reference (89)
□ Archive (58)
□ Stale (28)

SEARCH:
[________________]
```

#### Duplicate Groups Section

```
🔄 DUPLICATE PROJECTS ANALYSIS
═══════════════════════════════════════════════

Found 23 duplicate groups affecting 58 projects
Potential space savings: 18.7 GB

GROUP #1: "iot-sensor" project (Confidence: 95%)
├─ 📁 KEEP: ~/projects/iot-sensor
│  Size: 45 MB | Modified: 2024-09-12
│  Git: ✓ github.com/user/iot-sensor (main, 89 commits)
│  Completeness: 92% | Has: Tests, README, Docker
│  ✓ RECOMMENDED: Most recent, has remote, most complete
│
├─ 📁 DELETE: ~/Desktop/iot-sensor-backup
│  Size: 43 MB | Modified: 2023-11-05
│  Git: ✓ Local only (same history as above)
│  Completeness: 85% | Older version
│  🗑️ SAFE TO DELETE: Exact copy, older, no unique commits
│
└─ 📁 DELETE: ~/Documents/iot-sensor-old
   Size: 41 MB | Modified: 2023-08-12
   Git: ✗ No git
   Completeness: 78% | Very old backup
   🗑️ SAFE TO DELETE: Oldest version, no git

Actions: [Keep Recommended] [Review Differences] [Custom Selection]

GROUP #2: "home-automation" project (Confidence: 87%)
├─ 📁 KEEP: ~/projects/home-automation-esp32
│  Size: 12 MB | Modified: 2024-10-01
│  Git: ✓ github.com/user/home-automation (esp32-branch)
│  Platform: ESP32 | Completeness: 88%
│  ✓ RECOMMENDED: Active, ESP32 version
│
├─ 📁 ARCHIVE: ~/old-projects/home-automation-arduino
│  Size: 8 MB | Modified: 2022-03-10
│  Git: ✓ github.com/user/home-automation (arduino-branch)
│  Platform: Arduino Uno | Completeness: 85%
│  📦 DIFFERENT PLATFORM: This is Arduino version, above is ESP32
│  → RECOMMENDATION: Archive (might want to reference old Arduino code)
│
└─ 📁 DELETE: ~/Downloads/home-automation-copy
   Size: 12 MB | Modified: 2024-09-15
   Git: ✗ No git
   🗑️ SAFE TO DELETE: Temporary download, no unique changes

Actions: [Keep Recommended] [Review Code Differences] [Custom Selection]

... (continue for all 23 groups)

[Apply All Recommendations] [Review Each Group] [Export Report]
```

#### Obsolete/Incomplete Projects Section

```
🗑️ OBSOLETE & INCOMPLETE PROJECTS
═══════════════════════════════════════════════

Found 45 projects recommended for deletion
Potential space savings: 31.4 GB

OBSOLETE (No activity 5+ years, incomplete):
├─ ~/old-stuff/test-project-2018
│  Size: 234 MB | Last modified: 2018-06-12 (6+ years ago)
│  Type: Python | Completeness: 15%
│  Issues: Contains "test" in path, only 3 files, no git
│  🗑️ REASON: Very old test project, minimal code
│  [Delete] [Archive] [Keep]
│
├─ ~/Downloads/arduino-blink-copy
│  Size: 2 MB | Last modified: 2019-03-20 (5+ years ago)
│  Type: Arduino | Completeness: 25%
│  Issues: Basic example code, in Downloads
│  🗑️ REASON: Standard example, no custom code
│  [Delete] [Archive] [Keep]

INCOMPLETE (Started but never finished):
├─ ~/projects/temp-test
│  Size: 156 KB | Last modified: 2023-11-30
│  Type: Python | Completeness: 10%
│  Issues: Contains "temp" in path, only 1 file, no tests, no README
│  Git: ✓ 2 commits, all say "test"
│  🗑️ REASON: Temporary test, never developed
│  [Delete] [Archive] [Keep]

EMPTY/NEAR-EMPTY:
├─ ~/projects/new-project (empty - 0 files)
├─ ~/code/idea (1 file: notes.txt)
└─ ~/Desktop/untitled-folder (0 code files)
   Total: 12 empty project folders
   [Delete All] [Review] [Keep]

... (continue for all 45)

[Delete All Recommended] [Review Each] [Export List]
```

#### Project Relationships Graph

```
🔗 PROJECT RELATIONSHIPS
═══════════════════════════════════════════════

RELATED PROJECT GROUPS:

Group: "E-commerce Platform"
┌─────────────────────────────────────────┐
│ frontend-shop (React)                   │
│   ↓ API calls                           │
│ backend-api (.NET Core)                 │
│   ↓ uses                                │
│ shared-models (.NET Library)            │
│   ↓ database                            │
│ database-migrations (SQL)               │
└─────────────────────────────────────────┘
Location: All in ~/projects/ecommerce/
Status: Active, should stay together
Action: Keep as group in organized structure

Group: "IoT Home Automation"
┌─────────────────────────────────────────┐
│ esp32-sensor-nodes (C++)                │
│   → MQTT →                              │
│ mqtt-broker-config (Docker)             │
│   ← data ←                              │
│ data-processor (Python)                 │
│   → stores →                            │
│ mongodb-setup (Docker Compose)          │
│   ← reads ←                             │
│ dashboard-web (React)                   │
└─────────────────────────────────────────┘
Location: Scattered across ~/projects/, ~/esp32/, ~/web/
Status: Active multi-component system
Action: Consolidate into single organized location

SHARED LIBRARIES:
my-utils-library (Python)
  Used by: 12 projects
  Location: ~/projects/my-utils/
  → Should remain accessible to all projects

arduino-helpers (C++)
  Used by: 23 Arduino projects
  Location: ~/Arduino/libraries/arduino-helpers/
  → Keep in Arduino libraries folder

... (show all relationship groups)

[View Graph Visualization] [Export Relationships]
```

#### Code Mining - Reusable Components

```
💎 REUSABLE CODE DETECTED
═══════════════════════════════════════════════

Found valuable code worth extracting to a shared library:

HIGH VALUE COMPONENTS:
┌─ WPF Custom Controls Library
│  Found in: ~/projects/old-wpf-app/Controls/
│  Components: 15 custom WPF controls (well-documented)
│  Quality: High (unit tests, documentation)
│  Used in: 3 other projects
│  → RECOMMENDATION: Extract to ~/CodeLibrary/WPF/CustomControls
│  [Extract] [Review Code] [Skip]
│
├─ ESP32 WiFi Manager
│  Found in: ~/esp32/production-device/lib/wifi_manager/
│  Features: Auto-config, web portal, credential storage
│  Quality: Production-tested
│  Used in: 7 ESP32 projects (duplicated)
│  → RECOMMENDATION: Extract to ~/CodeLibrary/ESP32/WiFiManager
│  [Extract] [Review Code] [Skip]
│
├─ Python API Client Library
│  Found in: ~/projects/api-integration/client/
│  Features: Complete REST client with auth, retry logic
│  Quality: High (good error handling, typed)
│  Could be used in: 8 other Python projects
│  → RECOMMENDATION: Extract to ~/CodeLibrary/Python/APIClient
│  [Extract] [Review Code] [Skip]

USEFUL UTILITIES:
├─ Deployment Scripts (Bash)
│  Found in: ~/old-projects/deployment/scripts/
│  Features: Docker deployment, backup, rollback
│  Still relevant: Yes
│  → RECOMMENDATION: Extract to ~/CodeLibrary/Scripts/Deployment
│
├─ Database Migration Tools
│  Found in: ~/projects/old-backend/db/tools/
│  Features: Schema migration helpers
│  Still relevant: Yes
│  → RECOMMENDATION: Extract to ~/CodeLibrary/Database/MigrationTools

CONFIGURATION TEMPLATES:
├─ Working Docker Compose Templates
│  Found in: 5 different projects
│  Types: PostgreSQL, MongoDB, Redis, MQTT
│  → RECOMMENDATION: Consolidate to ~/CodeLibrary/Docker/Templates

... (list all valuable components)

[Extract All High Value] [Review Each] [Skip All]
```

#### Technology Dependency Analysis

```
⚠️ OUTDATED DEPENDENCIES & TECHNOLOGIES
═══════════════════════════════════════════════

DEPRECATED / END-OF-LIFE:
🔴 Python 2.7 (EOL 2020): 8 projects
   - ~/old-scripts/legacy-tool/ (2019)
   - ~/projects/old-web-scraper/ (2020)
   ... (list all)
   → RECOMMENDATION: Archive or upgrade to Python 3

🔴 .NET Framework 4.0 (EOL 2016): 12 projects
   - ~/projects/old-desktop-app/ (2019)
   ... (list all)
   → RECOMMENDATION: Upgrade to .NET 6+ or archive

🟡 Node.js 10.x (EOL): 6 projects
   → RECOMMENDATION: Update to Node 18 LTS

OUTDATED LIBRARIES:
🟡 Arduino IDE 1.0 projects: 23 projects
   → RECOMMENDATION: Migrate to Arduino 2.x or PlatformIO

🟡 Old ESP-IDF v3.x: 8 projects
   → RECOMMENDATION: Update to ESP-IDF v5.x

PROJECTS WORTH UPDATING:
List of otherwise good projects that need dependency updates:
- production-esp32-device (update ESP-IDF)
- customer-dashboard (update React 16 → 18)
- api-backend (update .NET Core 3.1 → .NET 8)

[Generate Update Plan] [Mark for Update] [Export List]
```

#### Missing Documentation Report

```
📝 PROJECTS MISSING DOCUMENTATION
═══════════════════════════════════════════════

Active/Important projects without README:
✗ ~/projects/iot-production-firmware (ACTIVE, 156 commits, no README!)
✗ ~/projects/client-dashboard (ACTIVE, 89 commits, no README!)
✗ ~/esp32/sensor-gateway (MAINTAINED, no README)
... (list 34 more)

[Generate Basic READMEs] [Review Each] [Skip]

Would auto-generate basic README with:
- Detected project type
- Technologies used
- Entry points identified  
- Last modified date
- Basic git stats
- "TODO: Add detailed documentation"
```

#### Export Options in HTML

- 📊 Export Full Report as JSON
- 📊 Export Full Report as CSV
- 📊 Export Git Inventory (separate)
- 📊 Export Security Report (separate)
- 📊 Export Duplicate Groups
- 📊 Export Reusable Components List
- 📊 Export as Markdown
- 📊 Generate PDF Summary Report
- 💾 Save Scan Results for Phase 2
- 📤 Export to Project Management Tool (Trello/Jira board format)

### Additional Phase 1 Features

**Search & Filter**: 
- Smart search box (searches names, paths, technologies, descriptions)
- Multi-select filters (combine any filters)
- Saved filter presets ("Show me problems", "Active projects only", etc.)
- Filter by type, size, date, status
- Filter by git status (has remote, local only, no git)
- Filter by remote host (GitHub, GitLab, etc.)
- Filter by issues (duplicates, incomplete, security, git issues)
- Filter by git health (healthy, needs attention, critical)
- Filter by activity level (ACTIVE/MAINTAINED/REFERENCE/ARCHIVE)
- Filter by technology stack

**Visual Charts & Graphs**:
- Timeline chart showing project activity over years
- Timeline of git commits over time (heatmap)
- Size distribution chart (histogram)
- Language/type breakdown (pie chart)
- Completeness score distribution (histogram)
- Git repository distribution by host (pie chart)
- Activity level breakdown (bar chart)
- Project relationships graph (interactive network diagram)
- Technology stack evolution timeline
- Commit activity by month/year (line graph)
- Top 10 largest projects (bar chart)
- Top 10 most active repos (bar chart)

**Smart Recommendations**:
- "You have 58 projects that haven't been touched in 3+ years"
- "23 duplicate groups detected - potential to save 18.7 GB"
- "45 projects are missing READMEs"
- "25 repositories are local-only and need remote backups"
- "38 repositories have uncommitted changes"
- "6 repositories have large files that should use Git LFS"
- "⚠️ 8 critical security issues need immediate attention"
- "4 nested .git directories should be cleaned up"
- "Quick wins available: 42.1 GB can be freed safely"
- "12 projects have valuable reusable code worth extracting"
- "18 projects need dependency updates"

**Git-Specific Insights**:
- "Most active repository: iot-platform with 892 commits"
- "Largest repository: machine-learning-project at 2.3 GB"
- "You have 15 unique contributors across all projects"
- "Total commits: 12,450 across 203 repositories"
- "Oldest git repository: first-arduino-project from 2018-02-14"
- "Most collaborative project: company-backend (12 contributors)"

**Configuration File Generation**:

Save scan results to:
- `code_inventory.json` - Complete project inventory
- `git_inventory.json` - Git-specific data
- `security_report.json` - Security findings
- `duplicates.json` - Duplicate groups
- `reusable_components.json` - Code mining results
- `relationships.json` - Project relationships

These will be used as input for Phase 2

---

## PHASE 2: CLEANING & RESTRUCTURING (Optional, Prompted)

This phase is COMPLETELY SEPARATE and only runs if explicitly invoked.
It uses the JSON files from Phase 1 as input.

### Pre-Phase 2: Impact Summary & Confirmation

Before ANY Phase 2 operations, show a comprehensive impact summary:

```
╔═══════════════════════════════════════════════════════════════════╗
║                    PHASE 2: PROPOSED CHANGES                       ║
╚═══════════════════════════════════════════════════════════════════╝

Based on your selections in Phase 1, here's what will happen:

📊 PROJECTS:
═══════════════════════════════════════════════════════════════════
✓ Will be kept & organized:     156 projects
📦 Will be archived:              89 projects  
💎 Will extract components from:  12 projects (then archive)
🗑️  Will be deleted:              45 projects
🎁 Quick wins cleanup:            Various build artifacts/caches

📤 GIT OPERATIONS:
═══════════════════════════════════════════════════════════════════
✓ Will be pushed to GitHub:      23 projects (currently local-only)
✓ Will commit stale changes:     12 projects (uncommitted >6mo)
✓ Will optimize (git gc):         6 large repositories
✓ Will add .gitignore to:        18 projects
✓ Will fix nested repos:          4 projects
✓ Will remove orphaned .git:      7 locations

💾 DISK SPACE:
═══════════════════════════════════════════════════════════════════
Current usage:                287.3 GB
After cleanup:                178.1 GB
Space freed:                  109.2 GB (38%)

Breakdown:
  - Quick wins (safe cleanup):     42.1 GB
  - Duplicates removed:            18.7 GB
  - Obsolete projects:             31.4 GB
  - Build artifacts:                3.2 GB
  - node_modules:                   8.4 GB
  - Old virtual envs:               4.2 GB
  - Misc caches:                    1.2 GB

📁 DIRECTORY STRUCTURE:
═══════════════════════════════════════════════════════════════════
Will create organized structure:

~/CodeOrganized/                 (156 active/maintained projects)
  ├── DotNet/
  │   ├── Desktop-Apps/          (35 projects)
  │   ├── Libraries/             (18 projects)
  │   └── Tools/                 (8 projects)
  ├── Python/
  │   ├── Web-Apps/              (15 projects)
  │   ├── Scripts/               (42 projects)
  │   ├── Data-Analysis/         (12 projects)
  │   └── Tools/                 (18 projects)
  ├── Embedded/
  │   ├── Arduino/               (28 active projects)
  │   ├── ESP32/                 (31 projects)
  │   ├── ESP8266/               (8 projects)
  │   └── RaspberryPi/           (7 projects)
  ├── Web/
  │   ├── Frontend/              (12 projects)
  │   ├── Backend/               (8 projects)
  │   └── Full-Stack/            (6 projects)
  ├── DevOps/
  │   ├── Docker/                (19 projects)
  │   ├── Kubernetes/            (4 projects)
  │   └── CI-CD/                 (5 projects)
  └── Scripts/
      ├── Bash/                  (23 scripts)
      ├── PowerShell/            (8 scripts)
      └── SQL/                   (31 scripts)

~/CodeArchive/                   (89 reference projects)
  └── (same structure, archived older projects)

~/CodeLibrary/                   (extracted reusable components)
  ├── WPF/
  │   └── CustomControls/
  ├── ESP32/
  │   ├── WiFiManager/
  │   └── SensorLibraries/
  ├── Python/
  │   ├── APIClient/
  │   └── Utilities/
  ├── Arduino/
  │   └── Helpers/
  └── Docker/
      └── Templates/

⏱️  TIME ESTIMATE:
═══════════════════════════════════════════════════════════════════
Scanning:                     Already complete ✓
Quick wins cleanup:           ~5 minutes
Extract reusable code:        ~10 minutes
Remove duplicates:            ~8 minutes
Remove obsolete:              ~5 minutes
Restructure projects:         ~45 minutes (moving 245 projects)
Git operations:               ~35 minutes
  - Push to GitHub (23):      ~15 minutes
  - Commit changes (12):      ~5 minutes
  - Add .gitignore (18):      ~3 minutes
  - Optimize repos (6):       ~10 minutes
  - Fix nested/orphaned:      ~2 minutes
Generate documentation:       ~3 minutes
──────────────────────────────────────────────────────────────────
Total estimated time:         ~111 minutes (~2 hours)

🔒 SAFETY MEASURES:
═══════════════════════════════════════════════════════════════════
✓ Full backup will be created before ANY changes
  Location: ~/CodeOrganization_Backups/2024-10-26_143022/
  Size: ~287 GB (full copy of everything)

✓ Git bundle backups for all repos being deleted
  Location: ~/CodeOrganization_Backups/2024-10-26_143022/git_bundles/

✓ Rollback script will be generated
  Can undo ALL changes if needed

✓ NO git repos with unpushed commits will be deleted
  (unless you explicitly force it with triple confirmation)

✓ All deletions require individual confirmation
  (or you can batch-approve by category)

✓ Dry-run available for any operation
  See exactly what will happen before it happens

⚠️  IMPORTANT NOTES:
═══════════════════════════════════════════════════════════════════
• Git operations require network access (for pushes)
• ~290 GB free space needed for backup + organized structure
• Projects will be MOVED, not copied (original locations emptied)
• IDE workspace files will be updated to new paths
• Docker compose files with relative paths will be updated
• You can skip any sub-phase if you change your mind

═══════════════════════════════════════════════════════════════════

How would you like to proceed?

[S] Start Phase 2 with all operations
[C] Customize (choose which operations to run)
[D] Dry-run first (see what would happen, no changes)
[E] Edit selections (go back to Phase 1 report)
[Q] Quit (don't organize, just keep the report)

Your choice:
```

### Sub-phases (each requiring confirmation)

#### 2A: Quick Wins Cleanup

```
═══════════════════════════════════════════════════════════════════
PHASE 2A: QUICK WINS CLEANUP
═══════════════════════════════════════════════════════════════════

This will safely remove build artifacts, caches, and temporary files.
These are zero-risk removals (can be regenerated).

Space to be freed: 42.1 GB

Operations:
✓ Remove empty folders (47)
✓ Remove node_modules in old projects (12 dirs, 8.4 GB)
✓ Remove build artifacts (23 locations, 3.2 GB)
✓ Remove __pycache__ (156 dirs, 287 MB)
✓ Remove .vs folders (31 dirs, 1.8 GB)
✓ Remove old virtual envs (18 dirs, 4.2 GB)
✓ Remove duplicate ZIPs (8 files, 2.1 GB)

Proceed with quick wins cleanup? (Y/n/customize):
```

#### 2B: Extract Reusable Components

```
═══════════════════════════════════════════════════════════════════
PHASE 2B: EXTRACT REUSABLE CODE
═══════════════════════════════════════════════════════════════════

Extract valuable code to ~/CodeLibrary/ for reuse:

Will extract:
1. WPF Custom Controls (15 controls from old-wpf-app)
   → ~/CodeLibrary/WPF/CustomControls/
   
2. ESP32 WiFi Manager (production-tested library)
   → ~/CodeLibrary/ESP32/WiFiManager/
   
3. Python API Client (REST client with auth)
   → ~/CodeLibrary/Python/APIClient/

... (list all 12)

After extraction, source projects will be archived.

Proceed? (Y/n/select):
```

#### 2C: Remove Duplicates

```
═══════════════════════════════════════════════════════════════════
PHASE 2C: REMOVE DUPLICATE PROJECTS
═══════════════════════════════════════════════════════════════════

Will process 23 duplicate groups:

Space to be freed: 18.7 GB

For each group, will:
- Keep the recommended version (most recent, most complete, has remote)
- Delete older copies
- Create backup before deletion

Duplicates summary:
  - Same project, different locations: 15 groups
  - Backup copies: 6 groups  
  - Downloaded copies: 2 groups

Show detailed plan for each group? (Y/n/just-proceed):

If Y:
  For each group:
    - Show all copies
    - Show recommendation
    - Prompt: Keep recommendation? (y/n/custom)
    - If custom: show detailed comparison, let user choose

If n:
  Apply all recommendations automatically
  (still creating backups)

Your choice:
```

#### 2D: Remove Obsolete Projects

```
═══════════════════════════════════════════════════════════════════
PHASE 2D: REMOVE OBSOLETE PROJECTS
═══════════════════════════════════════════════════════════════════

Will delete 45 projects identified as obsolete:

Categories:
  - Very old (5+ years, incomplete): 23 projects
  - Empty/near-empty folders: 12
  - Test/temp projects never developed: 10

Space to be freed: 31.4 GB

⚠️  Special cases requiring extra attention:
  - 3 projects have uncommitted changes (old, but not committed)
  - 1 project is local-only git repo (no remote backup)

Show list before deleting? (Y/n):

If Y:
  [List all 45 with details]
  Delete all? (Y/n/review-each)
  
If review-each:
  For each project:
    [Show details]
    Delete this? (y/n/archive-instead)
```

#### 2E: Git Repository Cleanup

```
═══════════════════════════════════════════════════════════════════
PHASE 2E: GIT REPOSITORY CLEANUP
═══════════════════════════════════════════════════════════════════

Multiple git maintenance operations:

1. Remove orphaned .git directories (7 locations)
   These are .git folders with no code
   Space: 234 MB
   [Proceed] [Skip]

2. Fix nested repositories (4 locations)
   Options for each:
   a) Convert to submodule
   b) Remove nested repo (flatten)
   c) Keep as-is
   [Review Each] [Skip All]

3. Optimize large repositories (6 repos >500MB)
   Run: git gc --aggressive, git prune
   Estimated time: ~10 minutes
   Potential space savings: ~800 MB
   [Proceed] [Skip]

4. Add missing .gitignore files (18 projects)
   Will generate appropriate .gitignore for each project type
   [Proceed] [Review Each] [Skip]

5. Commit stale changes (12 projects with uncommitted changes >6mo)
   Will prompt for commit message for each
   [Proceed Interactively] [Skip]

Select operations: (1,2,3,4,5 or 'all' or 'skip'):
```

#### 2F: Restructure into Organized Directory

```
═══════════════════════════════════════════════════════════════════
PHASE 2F: RESTRUCTURE INTO ORGANIZED DIRECTORIES
═══════════════════════════════════════════════════════════════════

Will move 245 projects into organized structure:
  - 156 to ~/CodeOrganized/ (active/maintained)
  - 89 to ~/CodeArchive/ (reference)

Destination:
  ~/CodeOrganized/  [Change location]
  ~/CodeArchive/    [Change location]

Operations that will be performed:
✓ Create directory structure
✓ Move projects to appropriate locations
✓ Update IDE workspace paths (.code-workspace, .vscode, etc.)
✓ Update Docker Compose relative paths
✓ Update git submodule references (if any)
✓ Create project index file (searchable catalog)
✓ Generate README for each category

Estimated time: 45 minutes
Disk space check:
  Required: ~156 GB
  Available: 287 GB
  ✓ Sufficient space

⚠️  Projects will be MOVED (not copied). Original locations will be empty.

Show detailed move plan? (Y/n/proceed):

If Y:
  [Table showing: Current Path → New Path for all 245]
  Proceed with moves? (Y/n)
```

#### 2G: Git Repository Initialization & Remote Setup

```
═══════════════════════════════════════════════════════════════════
PHASE 2G: GIT INITIALIZATION & REMOTE SETUP
═══════════════════════════════════════════════════════════════════

Two operations:

1. Initialize git for projects without version control (34 projects)
   Will:
   - Run git init
   - Create .gitignore (appropriate for project type)
   - Make initial commit
   - Optionally add remote
   
   Proceed? (Y/n/select):

2. Add remotes to local-only repos (25 projects)
   These projects have git but NO remote backup!
   
   Choose platform:
   [1] GitHub
   [2] GitLab  
   [3] Bitbucket
   [4] Azure DevOps
   [5] Custom/Self-hosted
   [6] Skip
   
   For GitHub selected:
     - Will use GitHub API to create repos
     - Need: Personal Access Token or SSH key
     - Prompt for: Public or Private repos
     - Create repos and add remotes
   
   Your choice:
```

#### 2H: Push to Remote (GitHub/GitLab/etc.)

```
═══════════════════════════════════════════════════════════════════
PHASE 2H: PUSH TO REMOTE REPOSITORIES
═══════════════════════════════════════════════════════════════════

Will push code to remote repositories:

1. New repos created in Phase 2G (23 projects)
   - Will be pushed to GitHub/GitLab
   
2. Repos with unpushed commits (8 projects)
   Project: mobile-app (23 unpushed commits)
   Project: iot-firmware (7 unpushed commits)
   ...

Before pushing, will:
✓ Scan for accidentally committed secrets
✓ Check .gitignore is present
✓ Verify remote connectivity
✓ Confirm repo visibility (public/private)

⚠️  Projects with security issues will be flagged and NOT pushed
    until issues are resolved.

Push configuration:
  Platform: GitHub
  Authentication: [SSH key] [Personal Access Token]
  Default visibility: [Private] [Public]
  
Proceed? (Y/n/configure):
```

#### 2I: Generate Missing Documentation

```
═══════════════════════════════════════════════════════════════════
PHASE 2I: GENERATE MISSING DOCUMENTATION
═══════════════════════════════════════════════════════════════════

34 important projects are missing README files.

Will auto-generate basic README.md for each with:
  - Project name and type
  - Technologies detected
  - Entry points (main files)
  - Dependencies
  - Last modified date
  - Git stats (if applicable)
  - Placeholder sections for:
    - Description (TODO: Add description)
    - Installation (TODO: Add instructions)
    - Usage (TODO: Add examples)
    - License

You can edit these READMEs later.

Generate READMEs? (Y/n/select-projects):
```

#### 2J: Generate Updated Documentation & Reports

```
═══════════════════════════════════════════════════════════════════
PHASE 2J: GENERATE FINAL DOCUMENTATION
═══════════════════════════════════════════════════════════════════

All operations complete! Generating final reports...

Will create:
1. Updated HTML report (before/after comparison)
2. Project catalog (searchable index of organized code)
3. What-was-done summary
4. Space savings report
5. Git operations log
6. New security status
7. Rollback instructions

[Generate Reports]
```

### After Completion

```
╔═══════════════════════════════════════════════════════════════════╗
║                    ORGANIZATION COMPLETE! 🎉                       ║
╚═══════════════════════════════════════════════════════════════════╝

SUMMARY:
═══════════════════════════════════════════════════════════════════

✅ COMPLETED OPERATIONS:
   ✓ Quick wins cleanup
   ✓ Extracted 12 reusable components
   ✓ Removed 23 duplicate groups (58 projects)
   ✓ Deleted 45 obsolete projects
   ✓ Fixed 7 orphaned .git directories
   ✓ Fixed 4 nested repositories
   ✓ Optimized 6 large repositories
   ✓ Organized 156 active projects
   ✓ Archived 89 reference projects
   ✓ Pushed 23 projects to GitHub
   ✓ Added .gitignore to 18 projects
   ✓ Generated 34 README files

📊 RESULTS:
   Projects before:    287
   Projects after:     245 (organized)
   Projects deleted:   45
   Duplicates removed: 58 (kept 23)
   
💾 DISK SPACE:
   Before:             287.3 GB
   After:              178.1 GB
   Freed:              109.2 GB (38%)

📁 YOUR CODE IS NOW ORGANIZED:
   ~/CodeOrganized/    - 156 active/maintained projects
   ~/CodeArchive/      - 89 reference projects  
   ~/CodeLibrary/      - 12 reusable component libraries

🔒 SAFETY:
   Backup location:    ~/CodeOrganization_Backups/2024-10-26_143022/
   Backup size:        287.3 GB
   Rollback script:    ~/CodeOrganization_Backups/2024-10-26_143022/ROLLBACK.sh
   
   To rollback everything: bash ROLLBACK.sh

📚 DOCUMENTATION:
   Full report:        ~/CodeOrganized/ORGANIZATION_REPORT.html
   Project catalog:    ~/CodeOrganized/PROJECT_CATALOG.json
   Git operations log: ~/CodeOrganized/GIT_OPERATIONS.log

📤 GIT STATUS:
   Total repositories: 203
   With remotes:       201 (99%)
   Local only:         2 (flagged for attention)
   Pushed today:       23 repos

🔒 SECURITY:
   Critical issues:    0 (all resolved! ✓)
   Warnings:           3 (reduced from 23)

═══════════════════════════════════════════════════════════════════

[Open Organization Report] [Open Project Catalog] [View Logs] [Exit]

Next steps:
1. Review the organized structure
2. Update any project-specific paths in external tools
3. Verify important projects are in correct locations
4. Delete backup after confirming everything works (~287 GB freed)
5. Consider removing old project folders that are now empty

Type 'help' for rollback instructions if needed.
```

### Phase 2 Safety Features

**Comprehensive Backup System**:
```
~/CodeOrganization_Backups/YYYY-MM-DD_HHMMSS/
├── full_backup/           # Complete copy of everything
├── git_bundles/           # Git bundle backups of all repos
├── metadata/
│   ├── inventory_before.json
│   ├── inventory_after.json
│   └── operations_log.json
├── ROLLBACK.sh            # Automated rollback script
└── README.txt             # What was backed up
```

**Git-Specific Safety**:
- NEVER delete a repo with unpushed commits without STRONG warning + triple confirmation
- NEVER delete a repo with uncommitted changes without backup
- Always verify remote connectivity before pushing
- Create bundle backups (.bundle files) of repos before deletion
- Verify git operations completed successfully
- Test pushed repos are accessible

**Rollback Capability**:
```bash
# Generated rollback script can:
- Restore all files from backup
- Restore git repos from bundles
- Undo all moves
- Restore original directory structure
- Undo git operations (remove remotes, restore refs)
```

**Confirmation at Every Step**:
- Never proceed without explicit user confirmation
- Extra confirmation for git operations
- Option to customize or skip any sub-phase
- Batch confirmations available (e.g., "delete all recommended")

**Dry-Run Mode**:
```bash
python code_organizer.py phase2 --dry-run --inventory code_inventory.json

Will show:
- Exactly what files would be moved where
- What would be deleted
- Git operations that would be performed
- Space that would be freed
- Time estimates
- NO ACTUAL CHANGES MADE
```

**Detailed Logging**:
```
~/CodeOrganization_Logs/YYYY-MM-DD_HHMMSS/
├── operations.log         # All operations with timestamps
├── git_operations.log     # Git-specific operations
├── errors.log             # Any errors encountered
├── moves.log              # All file moves
├── deletions.log          # All deletions
└── security_scan.log      # Security scans before git push
```

---

## Command-Line Interface Structure

### PHASE 1: SCAN & ANALYZE

```bash
# Quick scan (5-10 minutes)
python code_organizer.py scan-quick

# Full deep scan (30-60 minutes)
python code_organizer.py scan --output report.html --config scan_config.yaml

# Scan with specific focus
python code_organizer.py scan --focus git          # Deep git analysis
python code_organizer.py scan --focus security     # Security-focused scan
python code_organizer.py scan --focus duplicates   # Focus on finding dupes

# Scan specific directories only
python code_organizer.py scan --paths ~/projects ~/Desktop --output report.html

# View saved scan results
python code_organizer.py view-report report.html

# Interactive review mode
python code_organizer.py review --inventory code_inventory.json
```

### PHASE 2: ORGANIZE & CLEANUP

```bash
# Show impact summary before doing anything
python code_organizer.py plan --inventory code_inventory.json

# Run complete Phase 2 workflow (interactive, prompts at each step)
python code_organizer.py organize --inventory code_inventory.json

# Run specific Phase 2 operations only:
python code_organizer.py quick-wins --inventory code_inventory.json
python code_organizer.py extract-code --inventory code_inventory.json
python code_organizer.py remove-duplicates --inventory code_inventory.json
python code_organizer.py remove-obsolete --inventory code_inventory.json
python code_organizer.py git-cleanup --inventory git_inventory.json
python code_organizer.py restructure --inventory code_inventory.json --dest ~/CodeOrganized
python code_organizer.py git-init --inventory code_inventory.json
python code_organizer.py github-push --inventory code_inventory.json --token <PAT>
python code_organizer.py generate-docs --inventory code_inventory.json

# Dry run mode (see what would happen, make no changes)
python code_organizer.py organize --dry-run --inventory code_inventory.json
python code_organizer.py remove-duplicates --dry-run --inventory code_inventory.json

# Batch mode (auto-confirm all recommended actions, use with caution!)
python code_organizer.py organize --batch --inventory code_inventory.json
```

### GIT-SPECIFIC COMMANDS

```bash
python code_organizer.py git-status-all           # Show status of all repos
python code_organizer.py git-find-unpushed        # Find repos with unpushed commits
python code_organizer.py git-find-uncommitted     # Find repos with uncommitted changes
python code_organizer.py git-find-orphaned        # Find orphaned .git directories
python code_organizer.py git-find-local-only      # Find repos with no remote
python code_organizer.py git-optimize-all         # Run git gc on all repos
```

### UTILITY COMMANDS

```bash
# Rollback last operation
python code_organizer.py rollback --backup ~/CodeOrganization_Backups/2024-10-26_143022/

# Export reports in different formats
python code_organizer.py export --format json --inventory code_inventory.json
python code_organizer.py export --format csv --inventory code_inventory.json
python code_organizer.py export --format pdf --inventory code_inventory.json

# Check system for required tools
python code_organizer.py check-system

# Verify backup integrity
python code_organizer.py verify-backup --backup ~/CodeOrganization_Backups/2024-10-26_143022/
```

---

## Configuration File Example (scan_config.yaml)

```yaml
# ============================================================================
# PERSONAL PROFILE
# ============================================================================
personal_profile:
  developer_since: 2018              # Adjusts "old" thresholds
  primary_languages: [C++, C#, Python]
  primary_platforms: [Arduino, ESP32, ESP8266, Windows, Linux, RaspberryPi]
  primary_technologies: [WPF, Docker, IoT, Web]

# ============================================================================
# SCAN CONFIGURATION
# ============================================================================
scan:
  # Where to search
  search_paths:
    - "~"
    - "~/Desktop"
    - "~/Downloads"
    - "~/Documents"
    - "/mnt/projects"
  
  # What to exclude
  exclude_paths:
    - "/node_modules"
    - "/.venv"
    - "/venv"
    - "/env"
    - "/build"
    - "/dist"
    - "/bin"
    - "/obj"
    - "/.docker"
    - "/__pycache__"
    - "/.vs"
    - "/target"
    - "/Library"             # macOS system
    - "/System"              # macOS system
    - "/Windows"             # Windows system
    - "/Program Files"       # Windows system
    - "/Program Files (x86)" # Windows system
  
  # File patterns to search for
  file_patterns:
    dotnet: ["*.sln", "*.csproj", "*.vbproj", "*.fsproj"]
    python: ["*.py", "setup.py", "pyproject.toml", "requirements.txt"]
    arduino: ["*.ino", "platformio.ini"]
    cpp: ["*.cpp", "*.h", "CMakeLists.txt", "Makefile"]
    git: [".git", ".gitignore", ".gitattributes", ".gitmodules"]
    docker: ["Dockerfile", "docker-compose.yml", ".dockerignore"]
    web: ["package.json", "index.html", "*.html"]
  
  # Git analysis settings
  git_analysis:
    deep_scan: true                      # Analyze commit history, contributors
    check_remote_connectivity: true      # Test if remotes are reachable
    scan_for_large_files: true           # Find large files in git history
    large_file_threshold_mb: 100
    detect_nested_repos: true
    find_orphaned_git_dirs: true
    analyze_commit_messages: true        # Check quality of commit messages

  # Age thresholds
  obsolete_threshold_years: 5            # Projects older than this → obsolete
  reference_threshold_years: 2           # 2-5 years → reference
  active_threshold_months: 6             # < 6 months → active
  
  minimum_file_count: 3                  # Projects with fewer files → incomplete
  
# ============================================================================
# ORGANIZATION STRATEGY
# ============================================================================
organization_strategy:
  # Activity-based organization
  keep_archives_separate: true
  archive_location: "~/CodeArchive"
  extract_reusables: true
  reusables_location: "~/CodeLibrary"
  
  # How to group projects
  group_by: "technology"                 # Options: "technology", "date", "type", "client"
  
  # Target structure
  organized_location: "~/CodeOrganized"
  
  # What to do with various project types
  rules:
    active_projects: "organize"          # organize, archive, or keep-in-place
    maintained_projects: "organize"
    reference_projects: "archive"
    archived_projects: "archive"
    incomplete_projects: "prompt"        # Always ask what to do

# ============================================================================
# CLEANUP PREFERENCES
# ============================================================================
cleanup_preferences:
  aggressive_mode: false                 # Conservative for first run
  
  # Auto-cleanup (no prompting for these)
  auto_remove_build_artifacts: true      # bin/, obj/, build/, dist/
  auto_remove_empty_folders: true
  auto_remove_node_modules: true         # If not in active project
  auto_remove_pycache: true
  auto_remove_vs_folders: true           # .vs folders
  auto_remove_old_venvs: true
  
  # Prompting preferences
  batch_confirm_duplicates: false        # If true, confirm once for all dupes
  batch_confirm_obsolete: false          # If true, confirm once for all obsolete

# ============================================================================
# DUPLICATE DETECTION
# ============================================================================
duplicate_detection:
  similarity_threshold: 85               # Percent similarity to flag as duplicate
  use_content_hash: true                 # Hash files to find exact duplicates
  use_structure_compare: true            # Compare directory structure
  check_git_remotes: true                # Same remote URL = likely duplicate
  
  # Patterns that indicate duplicates
  duplicate_name_patterns:
    - "*-backup"
    - "*-old"
    - "*-copy"
    - "Copy of *"
    - "*-final"
    - "*-final-final"
    - "*-v2"
    - "*-temp"

# ============================================================================
# SECURITY SCANNING
# ============================================================================
security:
  scan_for_secrets: true
  scan_git_history: true                 # Check git history for secrets
  
  # What to look for
  secret_patterns:
    - "password\\s*=\\s*['\"](.+)['\"]"
    - "api_key\\s*=\\s*['\"](.+)['\"]"
    - "secret\\s*=\\s*['\"](.+)['\"]"
    - "AWS_SECRET_ACCESS_KEY"
    - "-----BEGIN PRIVATE KEY-----"
    - "-----BEGIN RSA PRIVATE KEY-----"
  
  # IoT/Embedded specific
  scan_for_iot_credentials: true
  iot_patterns:
    - "WiFi\\.begin\\(['\"](.+)['\"]\\s*,\\s*['\"](.+)['\"]\\)"  # Arduino WiFi
    - "const char\\* password\\s*=\\s*['\"](.+)['\"]"
    - "const char\\* ssid\\s*=\\s*['\"](.+)['\"]"
    - "mqtt.*password"
    - "MQTT.*PASSWORD"

# ============================================================================
# CODE MINING (Finding reusable code)
# ============================================================================
code_mining:
  enabled: true
  
  # What makes code "reusable"
  min_function_count: 5                  # Must have at least 5 functions
  min_documentation_score: 70            # Must be well-documented
  must_have_tests: false                 # Prefer tested code, but not required
  
  # Patterns that indicate libraries
  library_indicators:
    - "lib/"
    - "library/"
    - "utils/"
    - "helpers/"
    - "common/"
    - "shared/"

# ============================================================================
# REPORTING
# ============================================================================
reporting:
  output_format: "html"                  # html, json, markdown, pdf
  include_charts: true
  include_git_analytics: true
  include_code_mining: true
  include_relationship_graph: true
  include_timeline: true
  open_in_browser: true

# ============================================================================
# GIT OPERATIONS
# ============================================================================
git_operations:
  # GitHub settings
  github:
    default_visibility: "private"        # private or public
    create_repos_in_org: false           # If true, prompt for org name
    add_description: true                # Auto-add description from README
    add_topics: true                     # Auto-add topics based on tech stack
  
  # Commit settings
  auto_commit_message: "Organized by code_organizer"
  
  # Safety
  require_confirmation_for_push: true
  scan_for_secrets_before_push: true

# ============================================================================
# BACKUP
# ============================================================================
backup:
  create_backup: true
  backup_location: "~/CodeOrganization_Backups"
  include_git_bundles: true
  compress_backup: false                 # Set to true to save space (slower)
  
# ============================================================================
# LOGGING
# ============================================================================
logging:
  log_level: "INFO"                      # DEBUG, INFO, WARNING, ERROR
  log_location: "~/CodeOrganization_Logs"
  create_separate_git_log: true
```

---

## Technical Requirements

### Python Version
- **Python 3.10+** with type hints

### Required Libraries

- `rich` - Beautiful terminal output, progress bars, interactive prompts
- `pathlib` - Path operations
- `jinja2` - HTML report templating
- `gitpython` - Git operations (CRITICAL for git analysis)
- `PyGithub` - GitHub API
- `python-gitlab` - GitLab API
- `PyYAML` - Config file parsing
- `python-dotenv` - Environment file handling
- `click` - CLI framework (better than argparse)
- `pandas` - Data analysis for reporting
- `plotly` - Interactive charts for HTML report
- `hashlib` - File hashing for duplicate detection
- `difflib` - Content comparison
- `requests` - For checking remote connectivity
- `tqdm` - Additional progress bars
- `colorama` - Cross-platform colored terminal output
- `tabulate` - Pretty tables in terminal
- `questionary` - Interactive prompts
- `networkx` - For project relationship graphs
- `matplotlib` or `seaborn` - Additional charts

### Code Structure

```
code_organizer/
├── __init__.py
├── main.py                      # CLI entry point
├── config.py                    # Configuration management
│
├── phase1_scan/
│   ├── __init__.py
│   ├── scanner.py               # File system scanning
│   ├── quick_scanner.py         # Phase 1A quick scan
│   ├── analyzers.py             # Project analysis
│   ├── duplicate_detector.py    # Find duplicates
│   ├── security_scanner.py      # Security analysis
│   ├── git_analyzer.py          # Git-specific analysis
│   ├── code_miner.py            # Extract reusable components
│   ├── relationship_detector.py # Find related projects
│   ├── tech_analyzer.py         # Technology stack analysis
│   └── reporter.py              # Generate reports
│
├── phase2_organize/
│   ├── __init__.py
│   ├── impact_analyzer.py       # Pre-phase 2 impact summary
│   ├── quick_wins.py            # Quick wins cleanup
│   ├── code_extractor.py        # Extract reusable code
│   ├── cleaner.py               # Remove duplicates/obsolete
│   ├── restructurer.py          # Move/organize projects
│   ├── git_manager.py           # Git operations
│   ├── git_cleanup.py           # Git cleanup (orphaned, nested, etc.)
│   ├── github_manager.py        # GitHub operations
│   ├── gitlab_manager.py        # GitLab operations
│   ├── doc_generator.py         # Generate missing docs
│   └── final_reporter.py        # Final summary report
│
├── utils/
│   ├── __init__.py
│   ├── file_utils.py            # File operations
│   ├── git_utils.py             # Git helper functions
│   ├── backup.py                # Backup system
│   ├── rollback.py              # Rollback generator
│   ├── logger.py                # Logging
│   ├── progress.py              # Progress tracking
│   └── security_utils.py        # Security scanning helpers
│
├── interactive/
│   ├── __init__.py
│   ├── review_mode.py           # Phase 1C interactive review
│   ├── prompts.py               # All user prompts
│   └── drill_down.py            # Detailed project inspection
│
├── templates/
│   ├── report.html              # Main HTML report template
│   ├── styles.css               # Report styling
│   ├── charts.js                # Chart configurations
│   └── readme_template.md       # README template
│
├── config/
│   └── default_config.yaml      # Default configuration
│
└── tests/
    ├── __init__.py
    ├── test_scanner.py
    ├── test_duplicates.py
    ├── test_git_analyzer.py
    └── test_security.py
```

### Error Handling

- Graceful handling of permission errors
- Network error handling for GitHub/GitLab operations
- Git operation error handling (corrupted repos, etc.)
- Disk space validation before operations
- Input validation
- Interrupt handling (Ctrl+C gracefully)
- Automatic retry for network operations

### Performance Optimization

- Parallel scanning where possible (use multiprocessing)
- Lazy loading for large files
- Caching for repeated operations
- Progress tracking for long operations
- Efficient file hashing (read in chunks)

### Testing

- Unit tests for core functions
- Mock filesystem for testing
- Mock git operations for testing
- Test duplicate detection algorithm
- Test security scanning patterns
- Test git analysis functions
- Integration tests for Phase 2 operations

---

## Deliverables

1. **Complete Python package** with all modules
2. **Comprehensive README.md** with:
   - Installation instructions (pip install, venv setup)
   - Quick start guide
   - Detailed usage examples for both phases
   - Configuration guide
   - Git operation examples and best practices
   - Screenshots of HTML report
   - Security best practices
   - Troubleshooting guide (including git issues)
   - FAQ section
3. **Beautiful HTML report template** (responsive, interactive, with charts)
4. **Default configuration file** (well-commented)
5. **Example outputs** (anonymized):
   - Example scan results
   - Example HTML report (screenshots)
   - Example Phase 2 summary
6. **requirements.txt** with all dependencies
7. **setup.py** for easy installation
8. **Git operations guide** - detailed documentation on how git analysis and cleanup works
9. **Video tutorial** (optional but recommended) showing:
   - How to run Phase 1
   - How to interpret the report
   - How to use interactive review mode
   - How to run Phase 2 safely

---

## Key Success Principles

The key principles for this tool:

1. **Phase 1 is completely safe and read-only** (including git analysis)
2. **Phase 2 is powerful but heavily gated** with:
   - Clear impact summary BEFORE any changes
   - Confirmations at every step
   - Backups (including git bundles)
   - Rollback capability
   - Dry-run mode
3. **Git operations have extra safety checks** for uncommitted/unpushed work
4. **User is in control** - can customize, skip, or abort at any point
5. **Everything is documented and logged** - full audit trail
6. **Focus on real-world messiness** - handle all the edge cases of long-term development

This tool should make organizing years of scattered code feel safe, manageable, and even satisfying. The goal is to go from chaos to a clean, well-organized code library without losing anything important.
