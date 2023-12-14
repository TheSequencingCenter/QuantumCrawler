import os
import shutil
import sys

def searchdir():
    # Prompt the user for the top-level directory
    top_dir = input("Enter the full path to the top-level directory: ")

    # Check if the top-level directory exists
    if not os.path.exists(top_dir):
        print("Error: top-level directory does not exist.")
        sys.exit(1)  # Exit the script
        
    # Create 'fileset' directory
    fileset_dir = os.path.join(top_dir, 'fileset')
    os.makedirs(fileset_dir, exist_ok=True)

    # Prompt for file suffix
    file_suffix = input("Enter the file suffix (e.g., pdf, doc, xls): ")

    # Initialize counter for total number of files copied
    total_files_copied = 0

    # Recursively search and copy files
    for root, dirs, files in os.walk(top_dir):
        for file in files:
            if file.endswith('.' + file_suffix):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(fileset_dir, file)
                shutil.copy2(source_file, destination_file)
                total_files_copied += 1

    # Notify the user
    print(f"Total number of files copied: {total_files_copied}")
    print("Done.")

if __name__ == "__main__":
    searchdir()
