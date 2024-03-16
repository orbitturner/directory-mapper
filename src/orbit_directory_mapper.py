# orbit_directory_mapper.py
import argparse
import sys
from loguru import logger
from termcolor import colored
from art import text2art
from src.utils.arborescence_util import draw_directory_structure, create_directory, display_directory_format
from src.helpers.update_checker import check_for_update
from src.utils.settings_menu import edit_settings_menu

# ========================
# UTILS
# ========================
def print_colored_ascii_art():
    text = "Orbit Directory Mapper"
    colored_ascii_art = colored(text2art(text), 'cyan')
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
    from src.utils.settings_menu import Settings
    settings_manager = Settings()
    edit_settings_menu(settings_manager)
# ========================

# ========================
# MAIN
# ========================
def bootstrap():
    # Welcome message
    print_colored_ascii_art()
    parser = argparse.ArgumentParser(description="Display or Create a Folder Structure in a Second.")
    subparsers = parser.add_subparsers(title="Commands", dest="command", metavar="{view, create, check-update, settings}", required=True)

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

    logger.remove()
    # Configure logs with Loguru
    logger.add("logs/dirmap_events.log", rotation="10 MB", level="DEBUG")
    # Add another handler for the console, but only for INFO and higher levels
    logger.add(sys.stdout, level="INFO")

    # Execute the function associated with the sub-command
    if hasattr(args, 'func'):
        args.func(args)
    else:
        # If no sub-command is specified, execute the default command (view)
        check_for_update(args)



# ========================
# MAIN
# ========================
if __name__ == "__main__":
    bootstrap()
