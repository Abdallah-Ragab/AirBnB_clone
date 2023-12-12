import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()