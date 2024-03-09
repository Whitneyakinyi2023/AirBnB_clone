#!/usr/bin/python3
"""Console for our AirBnB clone"""


try:
    import gnureadline
    import sys
    sys.modules['readline']
except ImportError:
    pass

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

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

    def do_create(self, args):
        """creates new instance of BaseModel, saves it to JSON file,
        & prints the id"""
        if not args:
            print('** class name missing **')
            return

        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in globals():
            print('** class doesn\'t exist **')
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """prints string representation ofan instance"""
        arg_list = args.split()
        if not arg_list:
            print('** class name missing **')
            return

        class_name = arg_list[0]
        if class_name not in globals():
            print('** class doesn\'t exist **')
            return

        if len(arg_list) < 2:
            print('** instance id missing **')
            return

        obj_id = arg_list[1]
        obj_key = class_name + "." + obj_id
        if obj_key not in storage.all():
            print('** no instance found **')
            return

        print(storage.all()[obj_key])

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        arg_list = args.split()
        if not arg_list:
            print('** class name missing **')
            return

        class_name = arg_list[0]
        if class_name not in globals():
            print('** class doesn\'t exist **')
            return

        if len(arg_list) < 2:
            print('** instance id missing **')
            return

        obj_id = arg_list[1]
        obj_key = class_name + "." + obj_id
        if obj_key not in storage.all():
            print('** no instance found **')
            return

        del storage.all()[obj_key]
        storage.save()

    def do_all(self, args):
        """prints all string representation of all instances"""
        arg_list = args.split()
        obj_list = []
        if not args:
            for obj_key in storage.all():
                obj_list.append(str(storage.all()[obj_key]))
            print(obj_list)
            return

        class_name = arg_list[0]
        if class_name not in globals():
            print('** class doesn\'t exist **')
            return

        for obj_key in storage.all():
            if class_name in obj_key:
                obj_list.append(str(storage.all()[obj_key]))
        print(obj_list)

        def do_update(self, args):
            """update instance based on class name and id
            by adding/updating attribute"""
            arg_list = args.split()
            if not arg_list:
                print('** class name missing **')
                return

            class_name = arg_list[0]
            if class_name not in globals():
                print('** class doesn\'t exist **')
                return

            if len(arg_list) < 2:
                print('** instance id missing **')
                return

            obj_id = arg_list[1]
            obj_key = class_name + "." + obj_id
            if obj_key not in storage.all():
                print('** no instance found **')
                return

            if len(arg_list) < 3:
                print('** attribute name missing **')
                return

            attr_name = arg_list[2]
            if len(arg_list) < 4:
                print('** value missing **')
                return

            attr_value = " ".join(arg_list[3:])

            storage = self.storage
            obj = storage.all()[obj_key]
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
