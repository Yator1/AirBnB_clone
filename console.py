#!/usr/bin/python3

"""
A module that contains the entry point of the command interpreter
It contains a class HBNBCommand
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
            }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not arg:
            print('** class name missing **')
            return

        name = arg.split()[0]
        if name not in self.classes:
            print("** class doesn't exist **")
            return
        NewInstance = self.classes[name]()
        NewInstance.save()
        print(NewInstance.id)

    def do_show(self, arg):
        """Prints the string rep of an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        name = args[0]

        if name not in self.classes:
            print("** class doesn't exist **")
            return
        
        if  len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        inst_id = args[1]
        key = "{}.{}".format(name, inst_id)
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        name = args[0]
        inst_id = args[1]
        
        if name not in self.classes:
            print("** class doesn't exist **")
            return
        if inst_id == '':
            print("** instance id missing **")
            return

        objects = storage.all()
        key = "{}.{}".format(name, inst_id)
        
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")
        
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = storage.all()
        _list = []

        if not arg:
            for key in objects:
                _list.append(str(objects[key]))
        else:
            name = arg.split()[0]
            if name not in self.classes:
                print("** class doesn't exist **")
                return

            for key in objects:
                if key.split('.')[0] == name:
                    _list.append(str(objects[key]))
        print(_list)

    def do_update(self, arg):
        """
        Updates an instance based on class name/id by adding/updating attribute
        """
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        name = args[0]
        if name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
        objects = storage.all()
        inst_id = args[1]
        key = "{}.{}".format(name, inst_id)

        if key not in objects:
            print("** no instance found **")
            return
        attr_name = args[2]
        attr_value = args[3]

        if attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
            return
        instance = objects[key]
        setattr(instance, attr_name, attr_value)
        storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program"""
        print()
        return True
    def emptyline(self):
        """Do nothing on empty input."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
