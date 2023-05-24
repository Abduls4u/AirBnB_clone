#!/usr/bin/python3
''' A module that contains that contains the entry point of the co
mmand interpreter
Usage:
    ./console.py
Author:
    Abdulsalam Abdulsomad .A. - May 12th, 2023.
'''
import cmd
from models.base_model import BaseModel
CLASSES = [
   'BaseModel',
    ]


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

    def do_create(self, cls):
        '''Creates a new instance of BaseModel, saves it (to the
JSON file) and prints the id. Ex: $ create BaseModel'''
        if cls:
            if cls not in CLASSES:
                print("** class doesn't exist **")
            else:
                new_instance = eval(cls)()
                new_instance.save()
                print(new_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        '''Prints the string representation of an instance based
on the class name and id. Ex: $ show BaseModel 1234-1234-1234'''
        if args:
            cmd_args = args.split()
            cls = cmd_args[0]
            cls_id = cmd_args[1] if len(cmd_args) == 2 else None
            if cls:
                if cls not in CLASSES:
                    print("** class doesn't exist **")
                else:
                    from models import storage
                    dict_instance = storage.all()
                    key = "{}.{}".format(cls, cls_id)
                    if cls_id:
                        if key in dict_instance.keys():
                            print(dict_instance[key])
                        else:
                            print('** no instance found **')
                    else:
                        print('** instance id missing **')
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id
(save the change into the JSON file).Ex: $ destroy BaseModel 1234-1234-1234.'''
        if args:
            cmd_args = args.split()
            cls = cmd_args[0]
            cls_id = cmd_args[1] if len(cmd_args) == 2 else None
            if cls:
                if cls not in CLASSES:
                    print("** class doesn't exist **")
                else:
                    from models import storage
                    dict_instance = storage.all()
                    key = "{}.{}".format(cls, cls_id)
                    if cls_id:
                        if key in dict_instance.keys():
                            del dict_instance[key]
                            storage.save()
                        else:
                            print('** no instance found **')
                    else:
                        print('** instance id missing **')
        else:
            print("** class name missing **")

    def do_all(self, cls):
        '''Prints all string representation of all instances
based or not on the class name. Ex: $ all BaseModel or $ all'''
        from models import storage
        instances = storage.all().values()
        if cls:
            if cls not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(instance) for instance
                       in instances if cls in str(instance)])
        else:
            print([str(instance) for instance in instances])

    def do_update(self, args):
        '''Updates an instance based on the class name and id by
adding or updating attribute (save the change into the JSON file)
Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".'''
        from models import storage
        if args:
            cmd_args = args.split()
            cls = cmd_args[0]
            cls_id = cmd_args[1] if len(cmd_args) >= 2 else None
            attr = cmd_args[2] if len(cmd_args) >= 3 else None
            val = cmd_args[3] if len(cmd_args) >= 4 else None
            if cls:
                if cls not in CLASSES:
                    print("** class doesn't exist **")
                else:
                    dict_instance = storage.all()
                    key = "{}.{}".format(cls, cls_id)
                    if cls_id:
                        if key in dict_instance.keys():
                            if attr is None:
                                print('** attribute name missing **')
                            elif val is None:
                                print('** value missing **')
                            else:
                                instance = dict_instance[key]
                                if attr in type(instance).__dict__:
                                    val_type = type(instance.
                                                    __class__.
                                                    __dict__[attr])
                                    setattr(instance, attr, val_type(val))
                                else:
                                    setattr(instance, attr, val)
                        else:
                            print('** no instance found **')
                    else:
                        print('** instance id missing **')
        else:
            print("** class name missing **")
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
