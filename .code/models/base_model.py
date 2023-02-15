#!/usr/bin/python3
"""This defines the BaseModel Class"""
from models import storage
import uuid
from datetime import datetime

class BaseModel:
    """The BaseModel representation of the project"""
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel.
        Args:
            *args (any datatype)
            **kwargs (dict): key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updates_at = datetime.today()
        
        #Read in the key/pair attributes
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                        self.__dict__[key] = value
        else:
            storage.new() # models.storage.new(self)

    def save(self):
        """Updates attribute update_at with current datetime."""
        self.update_at = datetime.today()
        storage.save() # models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
