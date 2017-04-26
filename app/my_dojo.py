import random

from app.office import Office
from app.living_space import LivingSpace
from app.room import Room
from app.fellow import Fellow
from app.staff import Staff
from app.person import Person
from app.dojo import Dojo


class MyDojo(object):
    def __init__(self):
        self.rooms = []
        self.vacant_rooms = []
        self.offices = []
        self.vacant_offices = []
        self.livingspaces = []
        self.vacant_livingspaces = []
        self.people = []
        self.allocated_people = []
        self.unallocated_people = []
        self.fellows = []
        self.allocated_fellows = []
        self.staff = []
        self.allocated_staff = []

    def create_room(self, args):
        """Create new room(s)"""
        pass