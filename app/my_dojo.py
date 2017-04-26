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
        new_rooms = []
        for room_name in args["<room_name>"]:
            room_names_list = [room_object.name.upper() for room_object in self.rooms]
            if room_name.upper() in room_names_list:
                print('The room you tried to create already exists in the Dojo!')
                return
            elif args['livingspace']:
                new_room_object = LivingSpace(room_name)
                self.livingspaces.append(new_room_object)
                self.rooms.append(new_room_object)
                new_rooms.append(new_room_object)
            else:
                if args['office']:
                    new_room_object = Office(room_name)
                    self.offices.append(new_room_object)
                    self.rooms.append(new_room_object)
                    new_rooms.append(new_room_object)

        for new_room in new_rooms:
            print('An office called %s has been successfully created!' % str(new_room))
