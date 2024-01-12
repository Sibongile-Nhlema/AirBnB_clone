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


def handle_update_instance(instance, attribute_name, attribute_value):
    '''
    Handles updating an instance with the given attribute name and value.

    Args:
        instance: The instance to be updated.
        attribute_name: The name of the attribute to be updated.
        attribute_value: The value to be assigned to the attribute.
    '''
    if not attribute_name:
        print("** attribute name missing **")
    elif not attribute_value:
        print("** value missing **")
    else:
        setattr(instance, attribute_name, attribute_value)
        storage.save()

def parse(arg):
    '''
    Parses the line and returns the parsed elements
    '''
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

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

    def default(self, line):
        '''
        Handles the retrieval of the instances using the .all() method
        Usage: <class name>.all()
        '''
        '''
        read the line
        if match ".":
            if there is a valid class name and a valid command:
                execute the command
        '''
        new_list = line.split(".")
        command_dict = {
                "all()": "self.do_all(line)", 
                "count()": "self.do_count(line)",
                "show()": "self.do_show(line)",
                "destroy()": "self.do_destroy(line)",
                "update()": "self.do_update(line)"
                }

        if new_list[0] not in HBNBCommand.__classes or len(new_list) == 1:
            print("*** Unknown syntax: {}".format(line))
            return False
        else:
            pattern = r'show\("[\w-]+"\)'
            pattern_1 = r'destroy\("[\w-]+"\)'
            pattern_2 = r'update\([^)]*\)'
            matched = re.search(pattern, new_list[1])
            matched_1 = re.search(pattern_1, new_list[1])
            matched_2 = re.search(pattern_2, new_list[1])
            if matched:
                eval(command_dict["show()"])
            elif matched_1:
                eval(command_dict["destroy()"])
            elif matched_2:
                eval(command_dict["update()"])
            elif new_list[0] in HBNBCommand.__classes and new_list[1] in command_dict:
                eval(command_dict[new_list[1]])
            else:
                print("*** Unknown syntax: {}".format(line))

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

        # handle <class name>.show(<id>)
        if "." in args_line[0]:
            class_name = line.split(".")[0]
            uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
            uuid_match = re.search(uuid_pattern, line)
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            if uuid_match:
                extracted_uuid = uuid_match.group(0)
                instance_key = "{}.{}".format(class_name, extracted_uuid)
                print(all_instances[instance_key])
            else:
                print("** no instance found **")
        # Handle show <class_name>
        elif not args_line:
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

        # handle <class name>.destory(<id>)
        if "." in args_line[0]:
            class_name = line.split(".")[0]
            uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
            uuid_match = re.search(uuid_pattern, line)
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            if uuid_match:
                extracted_uuid = uuid_match.group(0)
                instance_key = "{}.{}".format(class_name, extracted_uuid)
                del all_instances[instance_key]
                storage.save()
            else:
                print("** no instance found **")

        # Handle destory(<id>)
        elif not args_line:
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

        # handle <class name>.all()
        if "." in ar_line[0]:
            class_name = line.split(".")[0]
            object_list = []

            for obj in storage.all().values():
                 if class_name == obj.__class__.__name__:
                     object_list.append(obj.__str__())
            print(str(object_list).replace('"', ""))

        # handle all <class name>
        elif len(ar_line) > 0 and ar_line[0] not in HBNBCommand.__classes:
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

        # handle <class name>.update(<id> <key> <value>)
        class_name = line.split(".")[0]
        uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        dict_pattern = r"\{[^}]*\}"
        uuid_match = re.search(uuid_pattern, line)
        dict_match = re.search(dict_pattern, args_line[1])

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if uuid_match:
            extracted_uuid = str(uuid_match.group(0))
            instance_key = "{}.{}".format(class_name, extracted_uuid)
            instance = all_instances[instance_key]
            if dict_match:
                # handle <class name>.update(<id> <dict>)
                new_dict = dict_match.group(0).replace("{", "").replace("}", "").replace(":", "")
                new = parse(new_dict)
                if len(new) % 2 == 0:
                    attribute_name = ""
                    attribute_value = ""
                    for i in range(len(new)):
                        if i % 2 == 0:
                            attribute_name = new[i]
                        else:
                            attribute_value = new[i]
                        if attribute_name and len(attribute_value) != 0:
                            handle_update_instance(instance, attribute_name, attribute_value)
                        else:
                            continue
                else:
                    for i in range(len(new)):
                        if i % 2 == 0:
                            print("** attribute name missing **")
                        else:
                            print("** value missing **")
            else:
                attribute_name = args_line[1]
                attribute_value = args_line[2].replace(")", "")
                handle_update_instance(instance, attribute_name, attribute_value)

        # handle update <class name>
        elif not args_line:
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
            handle_update_instance(instance, attribute_name, attribute_value)

    def do_count(self, line):
        '''Counts the number of instances of a class '''
        class_name = line.split(".")[0]
        instance_count = 0
        for obj in storage.all().values():
            if class_name == obj.__class__.__name__:
                instance_count += 1
        # should the result be returned instead??
        print(instance_count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
