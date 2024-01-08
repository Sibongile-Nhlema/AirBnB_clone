#!/usr/bin/python3
''' This is the module for the BaseModel Class '''

import uuid
from datetime import datetime


class BaseModel:
    ''' This class deinfes all common attributes for other classes '''
    def __init__(self):
        '''
        Constructor
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        Return a string representation
        '''
        return "[{}] ({}) {}".format(BaseModel.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''
        Updates the public instance attribute
        'updated_at' with current datetime
        '''
        self.updated_at = self.updated_at.now()

    def to_dict(self):
        '''
        Returns a dict containing all key/values of __dict__ of that instance
        '''
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        full_dictionary = self.__dict__
        full_dictionary['__class__'] = self.__class__.__name__
        return full_dictionary
