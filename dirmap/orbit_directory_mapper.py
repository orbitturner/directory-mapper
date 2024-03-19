# orbit_directory_mapper.py
import argparse
import sys
import os
from loguru import logger
from termcolor import colored
from art import text2art
from dirmap.utils.arborescence_util import draw_directory_structure, create_directory, display_directory_format
from dirmap.helpers.update_checker import check_for_update
from dirmap.utils.settings_menu import edit_settings_menu
from dirmap.helpers.manifest_helper import get_current_version, get_project_info

# ========================
# UTILS
# ========================
def print_colored_ascii_art():
    text = "Directory Mapper"
    colored_ascii_art = colored(text2art(text, "small"), 'cyan')
    print(colored_ascii_art)
# ========================

# ========================
# COMMANDS
# ========================
def view_command(args):
    logger.info(f"🌲 Operation Start 🌲")
    logger.info(f"📂 Folder Structure: {args.folder_path}")

    # Display the directory structure in the specified format
    if args.format:
        logger.info(f"📂 Displaying Directory Structure in {args.format.upper()} Format:\n")
        display_directory_format(args.folder_path, args.format, ignore_folders=args.ignore, ignore_regex=args.regex)
    else:   
        draw_directory_structure(args.folder_path, ignore_folders=args.ignore, ignore_regex=args.regex)

def create_command(args):
    logger.info(f"🌲 Operation Start 🌲")

    if args.description:
        create_directory(args.description, args.folder_path, ignore_folders=args.ignore, ignore_regex=args.regex)
    else:
        logger.error("❌ JSON description is required in create mode.")

def check_update_command(args):
    check_for_update()

def settings_menu_command(args):
    from dirmap.utils.settings_menu import Settings
    settings_manager = Settings()
    edit_settings_menu(settings_manager)

def version_command():
    # Get the current version and project information
    current_version = get_current_version()
    author, license = get_project_info()

    if current_version:
        print(f"➢ Current version: {current_version}\n")
    if author:
        print(f"\n⪢ Author: {author}")
    if license:
        print(f"⪢ License: {license}")
# ========================

# ========================
# MAIN
# ========================
def bootstrap():
    # Welcome message
    print_colored_ascii_art()
    parser = argparse.ArgumentParser(description="Display or Create a Folder Structure in a Second.")
    # Add parser for the version command
    parser.add_argument('-v', '--version', action='store_true', help="Display current version and project information", dest='version')
    subparsers = parser.add_subparsers(title="Commands", dest="command")

    # Parser for the view command
    view_parser = subparsers.add_parser("view", help="Display the structure of a folder (default)")
    view_parser.add_argument("folder_path", type=str, help="Path of the folder to explore or create")
    view_parser.add_argument("--ignore", type=str, nargs="*", help="Names of folders to ignore")
    view_parser.add_argument("--regex", type=str, help="Regex pattern to ignore certain folders")
    view_parser.add_argument("--format", choices=["json", "yaml"], help="Format of the directory structure (JSON or YAML)")
    view_parser.set_defaults(func=view_command)

    # Parser for the create command
    create_parser = subparsers.add_parser("create", help="Create a directory structure from a JSON description")
    create_parser.add_argument("folder_path", type=str, help="Path of the folder to explore or create")
    create_parser.add_argument("--ignore", type=str, nargs="*", help="Names of folders to ignore")
    create_parser.add_argument("--regex", type=str, help="Regex pattern to ignore certain folders")
    create_parser.add_argument("--description", type=str, help="JSON Content or Path of the JSON description file for create mode", required=True)
    create_parser.set_defaults(func=create_command)

    # Parser for the check-update command
    check_update_parser = subparsers.add_parser("check-update", help="Check for updates")
    check_update_parser.set_defaults(func=check_update_command)

    # Parser for the settings command
    settings_menu_parser = subparsers.add_parser("settings", help="Settings Menu")
    settings_menu_parser.set_defaults(func=settings_menu_command)

    args = parser.parse_args()

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logFileName = os.path.join(current_dir,"dirmap_logs", "dirmap_events.log")

    logger.remove()
    # Configure logs with Loguru
    logger.add(logFileName, rotation="10 MB", level="DEBUG")
    # Add another handler for the console, but only for INFO and higher levels
    logger.add(sys.stdout, level="INFO")

    # Check if -v or --version options are present
    if args.version:
        version_command()
    else:
        # Execute the function associated with the sub-command
        if hasattr(args, 'func'):
            args.func(args)
        else:
            # If no sub-command is specified, execute the default command (version and help)
            version_command()
            print("\n⮚⮚⮚⮚⮚⮚⮚⮚⮚⮚⮚⮚ ORBIT DIRECTORY MAPPER HELP MENU ⮘⮘⮘⮘⮘⮘⮘⮘⮘⮘⮘⮘\n")
            parser.print_help()




# ========================
# MAIN
# ========================
if __name__ == "__main__":
    bootstrap()
