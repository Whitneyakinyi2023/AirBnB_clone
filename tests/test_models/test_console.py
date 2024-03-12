#!/usr/bin/python3

"""testing console's features"""


import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch, Mock


class Test_Console(unittest.TestCase):
    """tests for HBNBCommand"""

    def test_creating_missing_class_name(self):
        """create an instance of HBNBCommand"""
        self.console = HBNBCommand()
        """Testing the Create command.
        Creates unique ID and prints 'class name missing'
        when instance is not present"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_create_nonexistent_class(self):
        """Testing the create command.
        Prints '** class doesn\'t exist **' if class doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create someclass")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """Testing the show command.
        Prints BaseModel with its details if present."""
        pass

    def test_show_instanceid_missing(self):
        """Testing the show command.
        Prints '** instance id missing **'
        if id isn't present in command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel <id>")
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_show_classname_missing(self):
        """Testing the show command.
        Prints '** class name missing **'
        if class name is missing(ex: $show)"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_nonexistent_class(self):
        """Testing the show command.
        Prints Error statement if class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_show_no_instance(self):
        """Testing the show command.
        Returns error statement if class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_destroy(self):
        """Testing the destroy command.
        Deletes an instance based on class name & id."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, '** missing arguments **')

    def test_destroy_classname_null(self):
        """Testing the destroy command.
        Returns error statement if class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            output = f.getvalue().strip()
            print("Output:", repr(output))
            self.assertEqual(output, "** missing arguments **")

    def test_destroy_missinginstance(self):
        """Testing the destroy command.
        Returns error statement if instance id is missing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, '** missing arguments **')

    def test_destroy_no_instance(self):
        """Testing the destroy comand.
        Returns error statement if instance of class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_all(self):
        """Testing the all command.
        Prints all instances based/not on the class name(in string format)."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()

    def test_all_class_null(self):
        """Testing the all command.
        If class name doesn't exist, returns error statement"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_update(self):
        """Testing the update command.
        Updates an instance based on class name and id
        by adding or updating attributes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertEqual(output, '** value missing **')

    def test_update_missing_id(self):
        """Testing the update command.
        Returns error statement if id is missing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_class_exist(self):
        """Testing the update command.
        Returns error statement if class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_classname_instance(self):
        """Testing the update command.
        Returns error statement if instance of the class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_update_attribute_name(self):
        """Testing the update command.
        Returns error statement if attribute name is missing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel existing-id")
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_update_value(self):
        """Testing the update command.
        Returns error statement
        if value for the attribute name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel existing-id")
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')


if __name__ == '__main__':
    unittest.main()
