#!/usr/bin/python3
'''Console Module'''
import cmd
# import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User


class HBNBCommand(cmd.Cmd):
    '''
    HBNBCommand class
    '''
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place','Review']

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, arg):
        '''EOF command to exit the program'''
        return True
    
    def emptyline(self):
        '''Empty line'''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            storage.save()
            print(new.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance'''
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''Prints all string representation of all instances'''
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items() if arg in key])

    def do_update(self, arg):
        '''Updates an instance based on the class name and id'''
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif len(arg.split()) == 2:
            print("** attribute name missing **")
        elif len(arg.split()) == 3:
            print("** value missing **")
        else:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                setattr(storage.all()[key], arg.split()[2], arg.split()[3])

                storage.all()[key].save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
