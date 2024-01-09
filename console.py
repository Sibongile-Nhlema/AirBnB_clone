#!/usr/bin/python3
''' This module conatins the entry point of the command interpreter '''

import cmd


class HBNBCommand(cmd.Cmd):
    '''
    This is the entry point for the command intepreter

    Features:
        - quit and EOF to exit porgram
        - help (updated and documented)
        - custom prompt (hbnb)
        - an empty line + ENTER has no effect

    Does NOT execute when imported
    '''
    prompt = "(hbnb) "

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

    def emptyline(self):
        '''
        Emptyline command has no effect/does nothing.
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
