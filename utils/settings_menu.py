from rich import print
from rich.prompt import Prompt
from utils.settings_manager import Settings

def display_settings(settings):
    print()
    print("[b]Current Settings:[/b]")
    for section, values in settings.items():
        print(f"[b]{section}:[/b]")
        for key, value in values.items():
            print(f"  {key}: {value}")

def edit_settings_menu(settings_manager):
    print()
    while True:
        print("[b]Settings Editor Menu[/b]")
        print("1. Display Current Settings")
        print("2. Edit Tree Builder Params")
        print("3. Reset Settings to Default")
        print("4. Exit")

        choice = Prompt.ask("Enter your choice (1-4):", choices=["1", "2", "3", "4"])

        if choice == "1":
            display_settings(settings_manager.settings)
        elif choice == "2":
            edit_tree_builder_params(settings_manager)
        elif choice == "3":
            settings_manager.reset_settings()
        elif choice == "4":
            break

def edit_tree_builder_params(settings_manager):
    print()
    current_params = settings_manager.get_tree_builder_params()

    print("[b]Current Tree Builder Params:[/b]")
    display_settings({"tree_builder": current_params})

    new_params = {}
    for key in current_params.keys():
        value = Prompt.ask(f"Enter new value for {key}:")
        new_params[key] = value

    settings_manager.update_tree_builder_params(new_params)
    print("[green]Tree Builder Params updated successfully![/green]")

if __name__ == "__main__":
    settings_manager = Settings()

    try:
        edit_settings_menu(settings_manager)
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")
