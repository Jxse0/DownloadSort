# DownloadSort

Automate file organization on Windows! This script allows users to specify a destination path and a parameter. When files with the specified parameter in their name are downloaded, the script automatically moves them to the specified destination. Simplify your file management and organize your downloads effortlessly.

## Steps to make it run:

1. Clone the repository.

    ```bash
    git clone https://github.com/Jxse0/DownloadSort.git
    ```

2. Create a file named `DownloadSort.txt` in the download folder. Each line in this file should contain the destination folder path followed by a semicolon and the parameter.

    Example `DownloadSort.txt` content:
    ```plaintext
    C:\Users\YourUsername\Documents\Downloads\Images;.img
    C:\Users\YourUsername\Documents\Downloads\Documents;.doc
    ```

    If the `DownloadSort.txt` file doesn't exist, the Python script will create the file for you and open a bash prompt where you can insert the destination and parameter.

3. Open the Task Scheduler on your Windows machine.

4. In the right-hand Actions pane, click on "Create Basic Task..."

5. Follow the wizard to set up a basic task. Provide a name and description for the task.

6. On the "Trigger" step, customize when the script should run.

7. On the "Action" step, choose "Start a program." Browse and select your `run_script.bat` file.

8. Complete the wizard, and you are done!

Now, the DownloadSort script will automatically organize your downloaded files based on the specified parameters and destination paths.
