import json


class FileStorage:
    __file_path = ""
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: v for k, v in json.load(f).items()}
        except FileNotFoundError:
            pass
