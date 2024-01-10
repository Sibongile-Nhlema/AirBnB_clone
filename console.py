#!/usr/bin/python3
''' This module conatins the entry point of the command interpreter '''

import re
import cmd
from shlex import split
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


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
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }

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

    def help_quit(self):
        ''' Documentation for the quit command '''
        print("Quit command to exit the program\n")

    def help_EOF(self):
        ''' Documentation for the EOF command '''
        print("EOF command cleanly quits/exits the program\n")

    def help_create(self):
        ''' Documentation for the create command '''
        print("Prints the string representation of an instance"
              " based on the class name and id. \nUsage: create <class>\n")

    def help_show(self):
        ''' Documentation for the show command '''
        print("Prints the string representation of an instance"
              "based on the class name and id."
              "\nUsage: show <class> <id> or <class>.show(<id>)\n")

    def help_destory(self):
        ''' Documentation for the destory command '''
        print("Deletes an instance based on the class name and id."
              "\nUsage: destroy <class> <id> or <class>.destroy(<id>)\n")

    def help_all(self):
        ''' Documentation for the all command '''
        print("Prints the string representation of all instances"
              "based or not on class name."
              "\nUsage: show <class> <id> or <class>.show(<id>)\n")

    def help_update(self):
        ''' Documentation for the update command '''
        print("Updates an instance based on the class name"
              "and id by adding or updating attribute."
              "\nUsage: update <class name> <id> <attribute name> "
              "'<attribute value>'\n")

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
        args_line = parse(line)
        all_instances = storage.all()

        if not args_line:
            print("** class name missing **")
        elif args_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_line[0], args_line[1]) not in all_instances:
            print("** no instance found **")
        elif len(args_line) == 2:
            print("** attribute name missing **")
        elif len(args_line) == 3:
            print("** value missing **")
        else:
            instance_key = "{}.{}".format(args_line[0], args_line[1])
            instance = all_instances[instance_key]
            attribute_name = args_line[2]
            attribute_value = args_line[3]

            if not attribute_name:
                print("** attribute name missing **")
            elif not attribute_value:
                print("** value missing **")
            else:
                setattr(instance, attribute_name, attribute_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
