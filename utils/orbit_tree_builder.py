import os
import pathlib
import sys
import re

from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree

def dir_tree_builder(directory: pathlib.Path, tree: Tree = None, ignore_folders=None, ignore_regex=None) -> None:
    """Recursively build a Tree with directory contents."""
    tree = Tree(
        f":open_file_folder: [link file://{directory}]{directory}",
        guide_style="bold bright_blue",
    ) if tree is None else tree
    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    for path in paths:
        # Remove hidden files
        if path.name.startswith("."):
            continue

        # Check if the current folder should be ignored
        if ignore_folders and path.name in ignore_folders:
            continue
        if ignore_regex and re.match(ignore_regex, path.name):
            continue

        if path.is_dir():
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
                style=style,
                guide_style=style,
            )
            dir_tree_builder(path, branch, ignore_folders, ignore_regex)
        else:
            text_filename = Text(path.name, "yellow")
            text_filename.highlight_regex(r"\..*$", "bold red")
            text_filename.stylize(f"link file://{path}")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            icon = "🐍 " if path.suffix == ".py" else "📄 "
            tree.add(Text(icon) + text_filename)
    return tree
