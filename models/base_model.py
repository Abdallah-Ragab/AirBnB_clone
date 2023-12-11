import datetime
import uuid


class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for kw in kwargs:
                if not kw == "__class__":
                    setattr(self, kw, kwargs[kw])

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        obj_dict = {}
        obj_dict["id"] = self.id
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict = {**obj_dict, **self.__dict__.copy()}
        return obj_dict
