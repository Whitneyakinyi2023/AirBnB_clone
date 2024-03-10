## AirBnB Clone Console

This project provides a command-line interface (CLI) for interacting with an AirBnB clone application. It allows you to create, show, and manage instances of BaseModel objects, which could represent listings, users, or other entities in your system.

## Command Interpreter

The project utilizes the cmd module in Python to create a simple command interpreter. Here's an overview of the available commands:

quit: Exits the console program.
show <class_name> <object_id>: Displays the string representation of an existing instance.
create <class_name>: Creates a new instance of the specified class, saves it, and prints the generated ID.
## Getting Started

Prerequisites:

Python 3 (tested with 3.x versions)
Installation:

Clone or download the project repository.
Navigate to the project directory in your terminal.
Make sure you have Python 3 and the cmd module installed. You can install it using pip install cmd.
Running the Console:

## Bash
python3 console.py or ./console.py
This will launch the interactive console where you can enter commands.

## Usage Examples

1. Creating a New Listing:

(hbnb) create User
f45d4s4d-1212-4d5f-9b9d-f5412312aefa
This creates a new User instance and prints its generated ID (which is a unique string).

2. Showing a Listing:

(hbnb) show User f45d4s4d-1212-4d5f-9b9d-f5412312aefa
<User id="f45d4s4d-1212-4d5f-9b9d-f5412312aefa" created_at="2024-03-10T20:05:30.078337">
This retrieves and displays the details of the User instance with the ID f45d4s4d-1212-4d5f-9b9d-f5412312aefa.

3. Exiting the Console:

(hbnb) quit
This will gracefully exit the console program.

## Additional Notes

Remember to replace <class_name> with the actual class name you want to interact with (e.g., User, Listing).
For the show command, provide both the class name and the ID of the specific instance you want to view.
Error messages will be displayed if you provide invalid commands or missing arguments.
This README provides a basic guide to using the AirBnB clone console. Feel free to explore further commands and functionalities based on your specific project requirements
