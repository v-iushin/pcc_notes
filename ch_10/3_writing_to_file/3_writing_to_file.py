# WRITING TO FILE

#! write_text() creates/rewrites the file

from pathlib import Path

BASE = Path(__file__).parent
path = Path(BASE/"programming.txt")
path.write_text("I love programming.")

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path.write_text(contents)
