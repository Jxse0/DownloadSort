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

            entries = os.scandir(downloads_path)

            for entry in entries:
                if para in entry.name:
                    destination_path = os.path.join(dst, entry.name)
                    if not os.path.exists(destination_path):
                        shutil.move(entry.path, destination_path)
                    else:
                        print(f"File '{entry.name}' already exists in '{dst}', skipping.")

if __name__ == "__main__":
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    sort_file_path = os.path.join(downloads_path, 'DownloadSort.txt')

    if os.path.exists(sort_file_path):
        move(sort_file_path)
    else:
        print('Creating DownloadSort.txt')
        open(sort_file_path, 'w').close()
        move(sort_file_path)
