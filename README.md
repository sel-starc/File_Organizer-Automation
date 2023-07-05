# File_Organizer-Automation


# File Organizer

## Description

The File Organizer script is a Python program that organizes files in a specified folder based on their file extensions. It creates subfolders in an output folder and copies files with matching extensions to their respective subfolders.

## Usage

1. Run the script by executing the following command: `python file_organizer.py`.
2. Enter the path of the folder to organize when prompted.
3. Enter the path of the output folder where the organized files will be copied.

## Example

```
Enter path of folder to organize: /path/to/source/folder
Enter path of output folder: /path/to/output/folder

Found extensions: txt, pdf, png, jpg

Organizing files...

- Moving all .txt files to /path/to/output/folder/txt
- Moving all .pdf files to /path/to/output/folder/pdf
- Moving all .png files to /path/to/output/folder/png
- Moving all .jpg files to /path/to/output/folder/jpg

File organization completed successfully.
```

## Requirements

- Python 3.x
- `pathlib` library
- `shutil` library

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request.

