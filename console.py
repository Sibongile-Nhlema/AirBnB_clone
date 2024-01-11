#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter.
"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def is_float(string):
    """
    Checks if a string is a floating point number.

    string (str): A string
    """

    if string.replace(".", "").isnumeric():
        return True
    else:
        return False


class HBNBCommand(cmd.Cmd):
    """
    The entry point of the command interpreter

    Commands:
    - quit: Exists the program.
    - create: Creates a new instance of BaseModel,
    saves it and prints the id.
    - show: Prints the string representation of an instance
    based on the class name and id.
    - destroy: Deletes an instance based on the class name and id.
    - all: Prints all string representation of all instances,
    based or not on the class name.
    - update: Updates an instance based on the class name and id
    by adding or updating attribute.
    """

    prompt = '(hbnb) '
    __classes = {
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review'
    }

    def do_create(self, line):
        """
        Creates a new instance of a class,
        saves it (to the JSON file) and prints the id.

        Args:
        - line (str): The command line
        """

        args = line.split()
        class_name = args[0] if args else None

        if not class_name:
            print("** class name missing **")
        elif (class_name not in HBNBCommand.__classes):
            print("** class doesn't exist **")
        else:
            new_instance = eval(class_name)()
            storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Args:
        - line (str): The command line
        """

        args = line.split()
        class_name = args[0] if args else None
        id = args[1] if len(args) > 1 else None

        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{id}"
            objects = storage.all()

            if key in objects:
                print(str(objects[key]))
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.

        Args:
        - line (str): The command line
        """

        args = line.split()
        class_name = args[0] if args else None
        id = args[1] if len(args) > 1 else None

        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{id}"
            objects = storage.all()

            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints string representation of all instances,
        based or not on the class name.

        Args:
        - line (str): The command line
        """

        if line:
            if line not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                str_representations = []
                for key, obj in objects.items():
                    if key.split('.')[0] == line:
                        str_representations.append(str(obj))
                print(
                    '[' +
                    ', '.join(f'"{str_repr}"'
                              for str_repr in str_representations)
                    + ']'
                    )
        else:
            objects = storage.all()
            str_representations = [f'"{str(obj)}"' for obj in objects.values()]
            print('[' + ', '.join(str_representations) + ']')

    def dot_notation_all(self, line):
        """
        Prints string representation of all instances,
        based or not on the class name.

        Args:
        - line (str): The command line
        """

        if line:
            if line not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                objects = storage.all()
                str_representations = []
                for key, obj in objects.items():
                    if key.split('.')[0] == line:
                        str_representations.append(str(obj))
                print(
                    '[' +
                    ', '.join(f'{str_repr}'
                              for str_repr in str_representations)
                    + ']'
                    )
        else:
            objects = storage.all()
            str_representations = [f'{str(obj)}' for obj in objects.values()]
            print('[' + ', '.join(str_representations) + ']')

    def dot_notation_show(self, class_name, instance_id):
        """
        Retrieves an instance based on its id.

        Args:
        - line (str): The command line
        """

        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{instance_id}"
            objects = storage.all()

            if key in objects:
                print(str(objects[key]))
            else:
                print("** no instance found **")

    def dot_notation_count(self, line):
        """
        Retrieves the number of instances of a class.

        Args:
        - line (str): The command line
        """

        count = 0
        objects = storage.all()

        for key in objects.keys():
            if key.split('.')[0] == line:
                count += 1

        print(count)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.

        Args:
        - line (str): The command line
        """

        args = line.split()
        class_name = args[0] if args else None
        id = args[1] if len(args) > 1 else None
        attr_name = args[2] if len(args) > 2 else None
        attr_value = args[3] if len(args) > 3 else None

        if attr_name and attr_name.startswith('"') and attr_name.endswith('"'):
            attr_name = attr_name.split('"')[1]
        if attr_name and attr_name.startswith("'") and attr_name.endswith("'"):
            attr_name = attr_name.split("'")[1]
        if (attr_value and attr_value.startswith('"')
                and attr_value.endswith('"')):
            attr_value = attr_value.split('"')[1]
        if (
                attr_value and attr_value.startswith("'")
                and attr_value.endswith("'")):
            attr_value = attr_value.split("'")[1]

        if attr_value and attr_value.isdigit():
            attr_value = int(attr_value)
        elif attr_value and is_float(attr_value):
            attr_value = float(attr_value)

        if not class_name:
            print("** class name missing **")
        else:
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif not id:
                print("** instance id missing **")
            else:
                key = f"{class_name}.{id}"
                objects = storage.all()

                if key in objects:
                    if not attr_name:
                        print("** attribute name missing **")
                    else:
                        if not attr_value:
                            print("** value missing **")
                        else:
                            obj = objects[key]
                            setattr(obj, attr_name, attr_value)
                            obj.save()
                else:
                    print("** no instance found **")

    def do_quit(self, line):
        """
        Exists the program.

        Args:
        - line (str): The command line
        """

        return True

    def default(self, line):
        """
        Handles unknown commands, allowing method calls with parentheses.

        Args:
        - line (str): The command line
        """

        match_all = re.match(r"^(.+)\.(.+)\((.*)\)$", line)
        if match_all:
            line = match_all.group(1)
            if match_all.group(2) == 'all':
                self.dot_notation_all(line)
            elif match_all.group(2) == 'count':
                self.dot_notation_count(line)
            elif match_all.group(2) == 'show':
                instance_id = match_all.group(3)
                self.dot_notation_show(line, instance_id)

    def help_create(self):
        """Prints documentation for create command."""

        print("Usage: create <class_name>")
        print("Create a new instance of a class")

    def help_show(self):
        """Prints documentation for show command."""

        print("Usage: show <class_name> <id>")
        print("Print the string representation of an instance.")

    def help_destroy(self):
        """Prints documentation for destroy command."""

        print("Usage: destroy <class_name> <id>")
        print("Delete an instance based on the class name and id.")

    def help_all(self):
        """Prints documentation for all command."""

        print("Usage: all <class_name>")
        print("Usage: all")
        print("Print string representation of all instances.")

    def help_update(self):
        """Prints documentation for update command."""

        print(
            "Usage: update <class_name> <id> "
            + "<attribute_name> <attribute_value>"
            )
        print("Update an instance based on the class name and id.")

    def help_quit(self):
        """Prints documentation for quit command."""

        print("Usage: quit")
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Does nothing"""

        pass

    def do_EOF(self, line):
        """
        Exits the program.
        """

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
