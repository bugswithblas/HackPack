#!/usr/bin/env python3

import argparse
import os
import yaml

# Directory where YAML files will be stored
COMMANDS_DIR = "commands"

def load_commands():
    """Load all commands from YAML files in the commands directory."""
    commands = {}
    if not os.path.exists(COMMANDS_DIR):
        os.makedirs(COMMANDS_DIR)
    for filename in os.listdir(COMMANDS_DIR):
        if filename.endswith(".yaml"):
            filepath = os.path.join(COMMANDS_DIR, filename)
            with open(filepath, "r") as file:
                category = os.path.splitext(filename)[0]
                commands[category] = yaml.safe_load(file) or []
    return commands

def list_categories(commands):
    """List all available categories."""
    return "\n".join(commands.keys())

def show_help(commands):
    """Show help information."""
    help_message = (
        "Usage: hackpack [CATEGORY]\n"
        "\n"
        "Categories:\n"
        f"{list_categories(commands)}\n"
        "\n"
        "Example:\n"
        "  hackpack nmap\n"
        "  hackpack xss\n"
    )
    return help_message

def main():
    commands = load_commands()
    
    parser = argparse.ArgumentParser(
        description="Hackpack: A CLI tool to display pentesting commands.",
        usage=show_help(commands),
        add_help=False
    )

    parser.add_argument(
        "category", 
        nargs="?", 
        help="The category of commands to display.", 
        choices=commands.keys(),
    )
    parser.add_argument(
        "-h", "--help", 
        action="store_true", 
        help="Show this help message and exit."
    )

    args = parser.parse_args()

    if args.help or not args.category:
        print(show_help(commands))
        return

    category = args.category
    if category in commands:
        print(f"Commands for {category}:")
        print("\n".join(commands[category]))
    else:
        print(f"Unknown category: {category}. Use -h for help.")

if __name__ == "__main__":
    main()
