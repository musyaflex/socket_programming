# socket_programming
This repository contains server-side and client-side code for a file transfer application using sockets in Python. The server-side code handles incoming connections, receives files or strings from clients, and performs appropriate actions based on the received commands. The client-side code connects to the server, sends commands and files/strings, and receives responses.

## Installation

The code does not have any external dependencies, so there is no need to install additional packages.

## Usage

It is recommended to create a virtual environment to isolate the project's dependencies.
You can use tools like PyCharm or create a virtual environment manually using venv module.
Activate the virtual environment before proceeding to the next steps.

### Running the server-side code:

Open the server.py file and modify the file_new_name variable to specify the path where you want to store the transferred files.
```py
# here you can change the path to save the file sent by client
file_new_name = os.path.join("C:\\",file_name)
```
Run the server.py file using Python.
The server will start listening for incoming connections on the specified IP address and port.

### Running the client-side code:

Open the client.py file.
Enter the IP address and port number of the server when prompted.
Follow the instructions on the command line to interact with the server.
You can use commands like POST_STRING, POST_FILE, GET, and EXIT to send strings or files to the server and retrieve messages/files from the server.

## Important points to note:

### Creating an executable 
If you want to distribute the application as an executable file (.exe), you can use tools like PyInstaller or Py2exe to package the Python code into a standalone executable. This step is optional and not required to run the code.

### Virtual environment 
It is recommended to use a virtual environment to manage the project's dependencies and avoid conflicts with other Python installations on your system. If you are using an IDE like PyCharm, it provides built-in support for creating and managing virtual environments.

### Modifying file storage path 
In the server-side code, there is a variable named file_new_name that specifies the path where the transferred files will be stored. By default, it is set to "C:\\", which is the root directory of the C: drive. You can change this path to any directory of your choice, depending on where you want to store the transferred files.
