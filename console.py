#!/usr/bin/python3
"""Console for our AirBnB clone"""


try:
    import gnureadline
    import sys
    sys.modules['readline']
except ImportError:
    pass

import cmd
"""Command line interpretor"""


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
