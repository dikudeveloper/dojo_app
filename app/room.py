from app.person import Person
from app.dojo import Dojo
from abc import ABCMeta, abstractmethod


class Room(object):
    def __init__(self):
        self.person = Person()
        self.dojo = Dojo()
        self.rooms = []

    @abstractmethod
    def get_room_availability(self):
        """Return the availability of the room"""
        pass