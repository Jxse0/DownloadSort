import os
import shutil

def move(sort_file):
    with open(sort_file, 'r') as f:
        downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')

        for line in f: 
            line = line.strip()
            split = line.split(';')
            dst = split[0].strip()
            para = split[1].strip()

            # Ensure the destination folder exists
            os.makedirs(dst, exist_ok=True)

            entries = os.scandir(downloads_path)

            for entry in entries:
                if para in entry.name:
                    destination_path = os.path.join(dst, entry.name)
                    try:
                        if not os.path.exists(destination_path):
                            shutil.move(entry.path, destination_path)
                            print(f"File '{entry.name}' moved to '{dst}'")
                        else:
                            print(f"File '{entry.name}' already exists in '{dst}', skipping.")
                    except (shutil.Error, FileNotFoundError, PermissionError) as e:
                        print(f"Error moving file '{entry.name}': {e}")

def get_input():
    while True:
        user_input = input("Enter a destination path and parameter separated by a semicolon (e.g., C:\\Path;parameter): ")
        split_input = user_input.split(';')

        if len(split_input) == 2 and os.path.isabs(split_input[0].strip()) and len(split_input[1].strip()) > 0:
            return user_input
        else:
            print("Invalid input. Please provide a valid path before the semicolon and a parameter after the semicolon.")

if __name__ == "__main__":
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    sort_file_path = os.path.join(downloads_path, 'DownloadSort.txt')

    if not os.path.exists(sort_file_path):
        print("DownloadSort.txt does not exist. Creating it.")
        open(sort_file_path, 'w').close()

    if os.stat(sort_file_path).st_size == 0:
        print("DownloadSort.txt is empty. Please provide input.")
        user_input = get_input()
        with open(sort_file_path, 'a') as sort_file:
            sort_file.write(user_input + '\n')

    move(sort_file_path)
