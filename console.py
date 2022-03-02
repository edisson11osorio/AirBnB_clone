#!/usr/bin/python3
"""Module for the HBNBCommand, set up and launch the console"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class to handle the console"""
    prompt = "(hbnb) "

    def do_create(self, line):
        """Create a new instance of a Model"""
        if line == "":
            print("** class name missing **")
        else:
            try:
                new_instance = globals()[line]()
                """-----Save the new instance-----"""
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            try:
                instance_to_show = globals()[tokens[0]]()
                if len(tokens) != 2:
                    print("** instance id missing **")
                else:
                    """-----Search in the storage-----"""
                    print(instance_to_show)
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            try:
                instance_to_destroy = globals()[tokens[0]]()
                if len(tokens) != 2:
                    print("** instance id missing **")
                else:
                    """-----Search in the storage-----"""
                    print(instance_to_destroy)
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Create a new instance of a Model"""
        if line == "":
            print("** class name missing **")
        else:
            try:
                new_instance = globals()[line]()
                """-----Save the new instance-----"""
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, line):
        """Shortcut command to exit the console typing Ctrl-D"""
        print("")
        return True

    def emptyline(self):
        """Disable the repetition of the last command when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
