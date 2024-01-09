#!/usr/bin/python3
''' This module conatins the entry point of the command interpreter '''

import re
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User


def parse(line):
    '''
    Parses the line and returns the parsed elements
    '''
    curly_match = re.search(r"\{(.*?)\}", line)
    bracket_match = re.search(r"\[(.*?)\]", line)

    if curly_match:
        lexer = line.split()[:curly_match.span()[0]]
        parsed_elements = [item.strip(",") for item in lexer]
        parsed_elements.append(curly_match.group())
    elif bracket_match:
        lexer = line.split()[:bracket_match.span()[0]]
        parsed_elements = [item.strip(",") for item in lexer]
        parsed_elements.append(bracket_match.group())
    else:
        parsed_elements = [item.strip(",") for item in line.split()]

    return parsed_elements


class HBNBCommand(cmd.Cmd):
    '''
    This is the entry point for the command intepreter

    Attributes:
        prompt (str): The command prompt.
        __classes (list): The list of commands.

    Features:
        - quit and EOF to exit porgram
        - help (updated and documented)
        - custom prompt (hbnb)
        - an empty line + ENTER has no effect

    Does NOT execute when imported
    '''
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User"}

    def do_quit(self, line):
        '''
        Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''
        EOF command cleanly quits/exits the program
        '''
        return True

    # To do: implement the custom help method
    def help_(self, line):
        '''
        Displays the help message for a specific command
        or lists all available commands

        Usage: help or help [command]

        Args:
            line (str): The input line containing the command name (optional).
        '''
        pass

    def emptyline(self):
        '''
        Emptyline command has no effect/does nothing.
        '''
        pass

    def do_create(self, line):
        '''
        Creates a new instance of BaseModel, saves it to a JSON file
        and prints the id

        Usage: create <class>

        Args:
            line (str): The input line containing the class name
        '''
        args_line = parse(line)
        arg_1 = args_line[0]
        if not args_line:
            print("** class name missing **")
        elif arg_1 not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_1)().id)
            storage.save()

    def do_show(self, line):
        '''
        Prints the string reprsentation of an instance
        based on the class name and id.

        Usage: show <class> <id> or <class>.show(<id>)

        Args:
            line (str): The input line containing the class name
        '''
        args_line = parse(line)
        all_instances = storage.all()
        if not args_line:
            print("** class name missing **")
        elif args_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_line) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args_line[0], args_line[1]) not in all_instances:
            print("** no instance found **")
        else:
            instance_key = "{}.{}".format(args_line[0], args_line[1])
            print(all_instances[instance_key])

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id

        Usage: destroy <class> <id> or <class>.destroy(<id>)

        Args:
            line (str): The input line containing the class name
        '''
        args_line = parse(line)
        all_instances = storage.all()
        if not args_line:
            print("** class name missing **")
        elif args_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_line) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args_line[0], args_line[1]) not in all_instances:
            print("** no instance found **")
        else:
            instance = "{}.{}".format(args_line[0], args_line[1])
            del all_instances[instance]
            storage.save()

    def do_all(self, line):
        '''
        Prints the string representation of all instances based or
        not on class name

        Usage: show <class> <id> or <class>.show(<id>)

        Args:
            line (str): The input line containing the class name
        '''
        ar_line = parse(line)
        if len(ar_line) > 0 and ar_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for obj in storage.all().values():
                if len(ar_line) == 0 or ar_line[0] == obj.__class__.__name__:
                    object_list.append(obj.__str__())
            print(object_list)

    def do_update(self, line):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Args:
            line (str): The input line containing the class name
        '''
        # To do: implement this function
        args_line = parse(line)
        all_instances = storage.all()

        if not args_line:
            print("** class name missing **")
        elif args_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_line) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args_line[0], args_line[1]) not in all_instances:
            print("** no instance found **")
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
