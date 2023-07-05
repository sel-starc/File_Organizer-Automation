from pathlib import Path
from shutil import copy
from sys import exit

input_path = Path(input("Enter path of folder to organize: "))
output_path = Path(input("Enter path of output folder: "))

if output_path.exists():
    print(f"ERROR: Output path {output_path} must not exist! Exiting.")
    exit(-1)

output_path.mkdir(exist_ok=True)

extensions = []
for item in input_path.iterdir():
    if item.is_file():
        extension: str = item.suffix[1:]
        extensions.append(extension)

print('Found extensions:', ', '.join(extensions))

for extension in extensions:
    current_dir = output_path / extension
    current_dir.mkdir(exist_ok=True)
    for item in input_path.iterdir():
        if not item.is_file():
            continue
        file_extension: str = item.suffix[1:]
        if file_extension != extension:
            continue
        copy(item, current_dir / item.name)
