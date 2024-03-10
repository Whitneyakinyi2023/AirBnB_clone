#!/usr/bin/python3
"""Console for our AirBnB clone"""

import cmd
from models.base_model import BaseModel
from models import storage


# Constants
PROMPT = '(hbnb) '
ERROR_CLASS_MISSING = '** class name missing **'
ERROR_INSTANCE_ID_MISSING = '** instance id missing **'
ERROR_VALUE_MISSING = '** value missing **'
ERROR_CLASS_DOESNT_EXIST = '** class doesn\'t exist **'
ERROR_INSTANCE_NOT_FOUND = '** no instance found **'



class HBNBCommand(cmd.Cmd):
    """Class representing the console for the AirBnB clone"""

    prompt = PROMPT

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles end of file signal"""
        print("^D")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def _create_instance(self, class_name):
        """Method to create instance of given class"""
        if not class_name:
            print(ERROR_CLASS_MISSING)
            return None
        if class_name not in globals():
            print(ERROR_CLASS_DOESNT_EXIST)
            return None
        new_instance = globals()[class_name]()
        new_instance.save()
        return new_instance

    def _get_instance_by_id(self, class_name, obj_id):
        """ Method to get instance by ID"""
        obj_key = f"{class_name}.{obj_id}"
        if obj_key not in storage.all():
            print(ERROR_INSTANCE_NOT_FOUND)
            return None
        return storage.all()[obj_key]

    def do_create(self, args):
        """Creates new instance of BaseModel, saves it to JSON file, and prints the ID"""
        class_name = args.split()[0]
        new_instance = self._create_instance(class_name)
        if new_instance:
            print(new_instance.id)

    def do_show(self, args):
        """Prints string representation of an instance"""
        arg_list = args.split()
        if len(arg_list) < 1:
            print(ERROR_CLASS_MISSING)
            return
        class_name = arg_list[0]
        if class_name not in globals():
            print(ERROR_CLASS_DOESNT_EXIST)
            return
        if len(arg_list) < 2:
            print(ERROR_INSTANCE_ID_MISSING)
            return
        obj_id = arg_list[1]
        obj = self._get_instance_by_id(class_name, obj_id)
        if obj:
            print(obj)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and ID"""
        arg_list = args.split()
        if len(arg_list) < 1:
            print(ERROR_CLASS_MISSING)
            return
        class_name, obj_id = arg_list[0], arg_list[1]
        obj = self._get_instance_by_id(class_name, obj_id)
        if obj:
            del storage.all()[f"{class_name}.{obj_id}"]
            storage.save()

    def do_all(self, args):
        """prints all string representation of all instances"""
        arg_list = args.split()
        if not arg_list:
            obj_list = [str(obj) for obj in storage.all().values()]
            print(obj_list)
            return
        class_name = arg_list[0]
        if class_name not in globals():
            print(ERROR_CLASS_DOESNT_EXIST)
            return
        obj_list = [str(obj) for key, obj in storage.all().items() if class_name in key]
        print(obj_list)

    def do_update(self, args):
        """Updates instance based on class name and ID"""
        arg_list = args.split()
        if len(arg_list) < 1:
            print(ERROR_CLASS_MISSING)
            return
        class_name, obj_id, *attr = arg_list
        if len(attr) < 2:
            print(ERROR_INSTANCE_ID_MISSING if len(attr) == 0 else ERROR_VALUE_MISSING)
            return
        attr_name, attr_value = attr[0], " ".join(attr[1:])
        obj = self._get_instance_by_id(class_name, obj_id)
        if obj:
            setattr(obj, attr_name, attr_value)
            obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
