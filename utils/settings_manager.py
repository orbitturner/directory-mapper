import json
import os
from loguru import logger


class Settings:
    def __init__(self, file_name="settings.json"):
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to the settings file
        self.file_path = os.path.join(current_dir,'..', file_name)
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as settings_file:
                settings_data = json.load(settings_file)
            return settings_data
        except FileNotFoundError:
            logger.error(f"❌ Settings file not found: {self.file_path}")
            raise FileNotFoundError("Settings file not found.")

    def get_tree_builder_params(self):
        return self.settings.get("tree_builder", {})

    def update_tree_builder_params(self, new_params):
        self.settings["tree_builder"].update(new_params)
        with open(self.file_path, "w", encoding="utf-8") as settings_file:
            json.dump(self.settings, settings_file, indent=4)
        logger.info("🌳 Tree Builder Params updated: {new_params}")

    def reset_settings(self):
        default_settings = {
            "tree_builder": {
                "guide_style": "bold #3a86ff",
                "folder_color": "#ff006e",
                "file_color": "#8338ec",
                "extension_color": "bold #ffbe0b",
                "file_size_color": "#fb5607",
                "python_files_icon": "🐍 ",
                "file_icon": "📄 ",
                "folder_icon": "📁 "
            }
        }

        with open(self.file_path, "w", encoding="utf-8") as settings_file:
            json.dump(default_settings, settings_file, indent=4)
        logger.info("🔄 Settings reset to default.")

# Example usage For Test Purposes:
# if __name__ == "__main__":
#     from loguru import logger

#     # Configure the logger
#     logger.add("settings.log", rotation="500 MB", level="INFO")

#     settings_manager = Settings()

#     # Get the tree builder parameters
#     tree_builder_params = settings_manager.get_tree_builder_params()
#     logger.info("🌳 Tree Builder Params: {tree_builder_params}")

#     # Update tree builder parameters
#     new_params = {
#         "folder_color": "cyan",
#         "file_color": "green",
#     }
#     settings_manager.update_tree_builder_params(new_params)

#     # Reset settings
#     settings_manager.reset_settings()
