# get-SHA-1-hash-of-file v1.2
The purpose: The purpose of this script is to check if a file exists, read the contents of the file as binary data, and then calculate and print the SHA-1 hash of the file. The script asks the user to enter the file name and then searches for the file using the os module. If the file is found, the script reads the contents of the file and calculates the SHA-1 hash of the file. The script then prints the SHA-1 hash of the file and waits for 10 seconds before closing the window.

This script is useful for verifying the integrity of a file. The SHA-1 hash of a file is a unique identifier that can be used to check if the contents of the file have been modified or corrupted in any way. By calculating the SHA-1 hash of the file and comparing it to a known good hash, you can be sure that the file has not been tampered with.

How-To:
To use this script, you will need to have the Python interpreter installed on your computer. You can download and install the Python interpreter from the official Python website https://www.python.org/downloads/

Once you have the Python interpreter installed, you can run the script by opening a terminal or command prompt, navigating to the directory where the script is located, and then running the following command:

python get-SHA-1-hash-of-file.py

This will start the Python interpreter and run the script. The script will then ask the user to enter the file name, search for the file, and calculate the SHA-1 hash of the file. The output will be displayed in the terminal or command prompt window.

It's important to note that the script will only be able to find the file if it's located in the same directory as the script, or if you provide the full path to the file. To ensure the script can locate the file, either place both the script and the file you want to check in the same directory or provide the complete file path when prompted.

How does it work?

The script starts by importing the hashlib, os, and time modules. The hashlib module is used to calculate the SHA-1 hash of the file, the os module is used to search for the file, and the time module is used to pause the script for a specified number of seconds before closing the window.

Next, the script defines the read_file() function, which is used to read the contents of the file as binary data. This function takes the file_name parameter, which is used to specify the file to read. The function opens the file in binary read-only mode ("rb") and reads the contents of the file. The function then returns the binary data.

After defining the read_file() function, the script prompts the user to enter the file name. The file name is stored in a variable called file_name.

Next, the script uses a while loop to search for the file using the os.path.exists() method. This method takes the file name as a parameter and returns True if the file exists, or False if the file does not exist. The while loop continues to run until the os.path.exists() method returns True, indicating that the file has been found. If the file is not found, the script will ask the user to enter the file name again.

Once a valid file name has been entered, the script calls the read_file() function to read the contents of the file as binary data. The read_file() function returns the binary data, which is stored in the file_contents variable.

Next, the script calculates the SHA-1 hash of the file contents. This is done by creating a new hashlib.sha1 object, which is used to calculate the SHA-1 hash of the file. The file_contents variable, containing the binary data, is passed directly to the sha1.update() method, which calculates the SHA-1 hash of the file. The resulting SHA-1 hash is stored in the file_hash variable.

Finally, the script prints the SHA-1 hash of the file using an f-string to include the file name in the output message. The script then waits for 10 seconds using the time.sleep() method, and then the window is closed.
