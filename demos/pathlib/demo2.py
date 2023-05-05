#!/usr/bin/env python3
from pathlib import Path

for file_path in Path.cwd().glob("*.txt"):
    new_path = Path("archive") / file_path.name
    file_path.replace(new_path)
