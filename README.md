# Installation

## 1. Install Dependencies

Ensure Python 3 and pip are installed:
```bash
sudo apt update && sudo apt install -y python3 python3-pip
```

Install the required Python package:
```bash
pip install pyyaml
```

## 2. Clone the Repository
```bash
git clone https://github.com/bugswithblas/hackpack.git
cd hackpack
```

## 3. Make the Script Executable
```bash
chmod +x hackpack
```

## 4. Move to /usr/local/bin for Global Access
```bash
sudo mv hackpack /usr/local/bin/
```

## 5. (Optional) Add an Alias
To make sure you can use Hackpack easily, add an alias to your shell profile:

For Bash users:
```bash
echo 'alias hackpack="/usr/local/bin/hackpack"' >> ~/.bashrc
source ~/.bashrc
```

For Zsh users:
```bash
echo 'alias hackpack="/usr/local/bin/hackpack"' >> ~/.zshrc
source ~/.zshrc
```

# Usage

```bash
hackpack [CATEGORY]
```

# Examples:

```bash
hackpack nmap   # Show Nmap commands
hackpack xss    # Show XSS commands
hackpack -h     # Show help
```

# Adding New Categories
To add a new category, create a YAML file inside the commands/ directory.

Example for csrf.yaml:

```yaml
- Check if CSRF tokens are missing or predictable.
- Use Burp Suite to test CSRF exploits.
```
