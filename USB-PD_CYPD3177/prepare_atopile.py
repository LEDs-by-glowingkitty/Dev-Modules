import os
import shutil
import sys

def generate_hierarchy(folder_path, level=0, output_file=None):
    """Generates a hierarchical overview of files and folders within a given directory.

    Args:
        folder_path (str): The path to the directory.
        level (int, optional): The indentation level for the output. Defaults to 0.
        output_file (file object, optional): An open file object to write the output to. 
                                              Defaults to None (prints to console).
    """
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        output_string = " " * level * 4 + "- " + item + "\n"
        if output_file:
            output_file.write(output_string)
        else:
            print(output_string, end="")
        if os.path.isdir(item_path):
            generate_hierarchy(item_path, level + 1, output_file)

def convert_ato_to_txt(folder_path):
    """Converts all .ato files in a directory to .txt files and places them in a separate folder.

    Args:
        folder_path (str): The path to the directory containing .ato files.
    """
    output_folder = os.path.join(folder_path, "txt_files")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith(".ato"):
            with open(os.path.join(folder_path, filename), "r") as ato_file, \
                 open(os.path.join(output_folder, filename[:-4] + ".txt"), "w") as txt_file:
                txt_file.write(ato_file.read())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    
    # Save hierarchy to a separate file
    hierarchy_file_path = os.path.join(folder_path, "hierarchy.txt")
    with open(hierarchy_file_path, "w") as hierarchy_file:
        print(f"## Folder Hierarchy (saved to {hierarchy_file_path}):")
        generate_hierarchy(folder_path, output_file=hierarchy_file)  # Write to file

    print("\n## .ato to .txt Conversion:")
    convert_ato_to_txt(folder_path)
    print("Conversion completed.")