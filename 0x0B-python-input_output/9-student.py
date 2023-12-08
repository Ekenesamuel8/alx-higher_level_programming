#!/usr/bin/python3
"""python input aNd output task 9"""


class Student:
    """class that defines student data
     Args:
         first_name (str): given name of student
         last_name (str): family name of student
         age (int): age of student in years

     Attributes:
         first_name (str): given name of student
         last_name (str): family name of student
         age (int): age of student in years
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
	self.last_name = last_name
	self.age = age

    def to_json(self):
    """retrieves a dictionary representation of a student instance
    """
    
        return self.__dict__ 
