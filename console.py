#!/usr/bin/python3
"""Module for the HBNBCommand, set up and launch the console"""
import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
                new_instance.save()
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based
            on the class name and id"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            try:
                globals()[tokens[0]]
                if len(tokens) != 2:
                    print("** instance id missing **")
                else:
                    all_data = storage.all()
                    key = tokens[0] + "." + tokens[1]
                    if key in all_data:
                        print(all_data[key])
                    else:
                        print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            try:
                globals()[tokens[0]]
                if len(tokens) != 2:
                    print("** instance id missing **")
                else:
                    all_data = storage.all()
                    key = tokens[0] + "." + tokens[1]
                    if key in all_data:
                        del all_data[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name"""
        len_line = len(line)
        tokens = line.split()
        if len_line > 0:
            try:
                globals()[tokens[0]]
                data_list = []
                all_data = storage.all()
                for data in all_data.values():
                    if tokens[0] == data.__class__.__name__:
                        data_list.append(data.__str__())
            except Exception:
                print("** class doesn't exist **")
                return
        else:
            data_list = []
            all_data = storage.all()
            for data in all_data.values():
                data_list.append(data.__str__())
        print(data_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            try:
                globals()[tokens[0]]
            except Exception:
                print("** class doesn't exist **")
                return
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            else:
                all_data = storage.all()
                key = tokens[0] + "." + tokens[1]
                if key in all_data:
                    value_key = all_data.get(key)
                    if len(tokens) < 3:
                        print("** attribute name missing **")
                        return
                    else:
                        if len(tokens) < 4:
                            print("** value missing **")
                            return
                        else:
                            value = tokens[3]
                            try:
                                value = int(tokens[3])
                            except Exception:
                                pass
                            setattr(value_key, tokens[2], value)
                            setattr(value_key, "updated_at", datetime.now())
                            all_data[key] = value_key
                            storage.save()
                else:
                    print("** no instance found **")

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        number_instances = 0
        for inst in storage.all().values():
            if inst.__class__.__name__ == line:
                number_instances += 1
        print(number_instances)

    def default(self, line):
        """Check if an input is valid an call the associated method"""
        switcher = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show
        }

        tokens = line.split(".")
        name_model = tokens[0]
        command_do = tokens[1].split("(")[0]

        if command_do in switcher.keys():
            method_call = switcher.get(command_do)
            if command_do == "show":
                id = tokens[1].split("(\"")[1]
                return method_call(name_model + " " + id.split("\")")[0])
            return method_call(name_model)
        return

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, line):
        """Shortcut command to exit the console typing Ctrl-D"""
        print("")
        return True

    def emptyline(self):
        """Disable the repetition of the last command when
            an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
