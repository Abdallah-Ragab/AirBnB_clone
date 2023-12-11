#!/usr/bin/python3

import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for kw in kwargs:
                if kw == "created_at" or kw == "updated_at":
                    setattr(self, kw, datetime.datetime.strptime(
                        kwargs[kw], "%Y-%m-%dT%H:%M:%S.%f"))
                if not kw == "__class__":
                    setattr(self, kw, kwargs[kw])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
