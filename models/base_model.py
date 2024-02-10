#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    A class basemodel
    """

    def __init__(self, *args, **kwargs):
        """
        initializes the base model instances
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                else:
                    self.__dict__[key] = value

                if key in ("created_at", "updated_at"):
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = time
        else:
            self.id = str(uuid.uuid4());
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        returning string rep of the instances
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["created_at"] = self.created_at.isoformat()
        return obj_dict
