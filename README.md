# Python Command-Line Tools

This repository is a collection of command-line tools built with Python to automate and simplify various tasks.

## Table of Contents
- [Setup](#setup)
- [Scripts](#scripts)
  - [search.py](#searchpy)
- [Configuration](#configuration)
  - [.gitignore](#gitignore)
  - [EXAMPLE_POWERSHELL_PROFILE.txt](#example_powershell_profiletxt)
- [License](#license)

## Setup

To use these scripts, you need to have Python installed on your system. You can then run them from the command line. For a better experience, you can create aliases or functions in your shell profile to run the scripts with shorter commands.

For example, you can add the following function to your PowerShell profile to create an `s` command that runs the `search.py` script:

```powershell
function s {
  python C:\Users\migue\CustomScripts\python\search.py $args
}
```

*Remember to replace `C:\Users\migue\CustomScripts\python\search.py` with the actual path to the script on your system.*

## Scripts

### search.py
This script allows you to quickly perform a Google search from your command line. It opens the search results in the Microsoft Edge browser.

**Usage:**
```bash
python search.py your search query
```

You can also search within a specific website using the `-s` or `--site` flag:
```bash
python search.py your search query -s example.com
```

## Configuration

### .gitignore
This file specifies which files and directories should be ignored by Git. In this project, it's configured to ignore IDE-specific files (`.idea`) and Python virtual environments (`.venv`).

### EXAMPLE_POWERSHELL_PROFILE.txt
This file provides an example of how to create a PowerShell function to act as a convenient alias for the `search.py` script. See the [Setup](#setup) section for more details.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.
