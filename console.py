#!/usr/bin/python3
''' A module that contains that contains the entry point of the co
mmand interpreter
Usage:
    ./console.py
Author:
    Abdulsalam Abdulsomad .A. - May 12th, 2023.
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''HBNB console(command line intepreter)'''
    prompt = '(hbnb) '
    def do_quit(self, args):
        '''Quits the console'''
        return (True)

    def do_EOF(self, args):
        '''Exits the console'''
        print()
        return (True)

    def emptyline(self):
        '''Executes nothing if line is empty'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
