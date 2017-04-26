
class Room(object):
    """Creates a Room object"""
    def __init__(self, name):
       self.occupants = []
       self.name = name

    def __repr__(self):
        return "<Room %s>" % self.name