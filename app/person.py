# Person class
# Creates a Person object that Fellow and Staff classes inherit from


class Person(object):
    """Creates a Person object that Fellow and Staff class inherit from"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Person %s>" % self.name