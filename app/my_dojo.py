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
        self.empty_rooms = []
        self.empty_livingspaces = []
        self.empty_offices = []
        self.offices = []
        self.livingspaces = []
        self.people = []
        self.allocated_people = []
        self.unallocated_people = []
        self.allocated_fellows = []
        self.allocated_staff = []
        self.fellows = []
        self.staff = []

    def create_room(self, args):
        """Create new room(s)"""
        new_rooms = []
        for room_name in args['<room_name>']:
            room_names_list = [room_object.name.upper() for room_object in self.rooms]
            if room_name.upper() in room_names_list:
                print('The room you tried to create already exists in the Dojo!')
                return
            elif args['livingspace']:
                new_livingspace_object = LivingSpace(room_name)
                self.livingspaces.append(new_livingspace_object)

                # mark new Living space and room as empty/vacant
                for livingspace in self.livingspaces:
                    if len(livingspace.occupants) < livingspace.capacity:
                        if livingspace not in self.empty_livingspaces:
                            self.empty_livingspaces.append(livingspace)
                            self.empty_rooms.append(livingspace)
                    elif len(livingspace.occupants) >= livingspace.capacity:
                        if livingspace in self.empty_livingspaces:
                            self.empty_livingspaces.remove(livingspace)
                            self.empty_rooms.remove(livingspace)
                self.rooms.append(new_livingspace_object)
                new_rooms.append(new_livingspace_object)
            else:
                if args['office']:
                    new_office_object = Office(room_name)
                    self.offices.append(new_office_object)

                    # mark new office and room as empty/vacant
                    for office in self.offices:
                        if len(office.occupants) < office.capacity:
                            if office not in self.empty_offices:
                                self.empty_offices.append(office)
                                self.empty_rooms.append(office)
                        elif len(office.occupants) >= office.capacity:
                            if office in self.empty_offices:
                                self.empty_offices.remove(office)
                                self.empty_rooms.remove(office)
                    self.rooms.append(new_office_object)
                    new_rooms.append(new_office_object)

        for new_room in new_rooms:
                print('An %s called %s has been successfully created!' % (new_room.room_type, str(new_room)))

    def add_person(self, args):
        """Add new person"""
        name = args['<first_name>'] + ' ' + args['<last_name>']
        wants_space = 'Yes' if args.get('<wants_accommodation>') is 'Y' else 'N'

        # checks for empty rooms
        # self.get_status_of_empty_rooms()

        # If there are no empty rooms;
        # if not self.empty_offices:
        #     print('Sorry, there are no available offices at this time!')
        #     print('Create a new office using the <create_room> command')
        #     return

        # Both STAFF and FELLOW must get an Office Randomly
        office_choice = random.choice(self.empty_offices)

        if args['<STAFF>']:
            new_person = Staff(name)
            self.staff.append(new_person)
            office_choice.occupants.append(new_person)
            self.allocated_staff.append(new_person)
            self.allocated_people.append(new_person)
            print('Staff %s %s has been successfully added.' % (args['<first_name>'], args['<last_name>']))
            print('%s has been allocated the office %s' % (args['<first_name>'], office_choice))
        elif args['<FELLOW>']:
            new_person = Fellow(name)
            self.fellows.append(new_person)
            office_choice.occupants.append(new_person)
            self.allocated_fellows.append(new_person)
            self.allocated_people.append(new_person)
            print('Fellow %s %s has been successfully added.' % (args['<first_name>'], args['<last_name>']))
            print('%s has been allocated the office %s' % (args['<first_name>'], office_choice))

            # If wants accommodation
            if wants_space == 'Yes':
                if len(self.empty_livingspaces) == 0:
                    print('Sorry, there are no available Living Spaces at this time!')
                    print('Create a new Living Space using the <create_room> command')
                    return
                # assign FELLOW a random living space
                livingspace_choice = random.choice(self.empty_livingspaces)
                livingspace_choice.occupants.append(new_person)
                print('%s has been allocated the livingspace %s' % (args['<first_name>'], livingspace_choice))

    def get_status_of_empty_rooms(self):
        """empty offices and empty livingspaces"""
        for office in self.offices:
            if len(office.occupants) < office.capacity:
                if office not in self.empty_offices:
                    self.empty_offices.append(office)
                    self.empty_rooms.append(office)
            elif len(office.occupants) >= office.capacity:
                if office in self.empty_offices:
                    self.empty_offices.remove(office)
                    self.empty_rooms.remove(office)
        for livingspace in self.livingspaces:
            if len(livingspace.occupants) < livingspace.capacity:
                if livingspace not in self.empty_livingspaces:
                    self.empty_livingspaces.append(livingspace)
                    self.empty_rooms.append(livingspace)
            elif len(livingspace.occupants) >= livingspace.capacity:
                if livingspace in self.empty_livingspaces:
                    self.empty_livingspaces.remove(livingspace)
                    self.empty_rooms.remove(livingspace)