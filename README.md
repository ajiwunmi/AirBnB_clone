# AirBnB clone - The console

![AirBnB Project logo](images/airbnb.png)

The AirBnB clone project objective is to deploy on your server a simple copy of the AirBnB website.

in the project some feactures will be implemented. These includes:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Command Interpreter

Command Interpreter, just like the Shell, it's exactly the same but limited to a specific use-case. The objective of this, is that we want to be able to manage the objects of our project(the models):

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.

| Command                                       | Example                                                                                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Run the console                               | `./console.py`                                                                                                                            |
| Quit the console                              | `(hbnb) quit`                                                                                                                             |
| Display the help for a command                | `(hbnb) help <command>`                                                                                                                   |
| Create an object (prints its id)              | `(hbnb) create <class>`                                                                                                                   |
| Show an object                                | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)`                                                                                 |
| Destroy an object                             | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)`                                                                           |
| Show all objects, or all instances of a class | `(hbnb) all` or `(hbnb) all <class>`                                                                                                      |
| Update an attribute of an object              | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |
