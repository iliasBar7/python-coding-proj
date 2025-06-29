class Student:
    def __init__(self, id, firstname, lastname):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self.__id = value

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string")
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string")
        self.__lastname = value
