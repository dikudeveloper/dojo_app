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
        """Add a new person"""
        first_name = args['<first_name>']
        last_name = args['<last_name>']
        fellow = args['Fellow']
        staff = args['Staff']
        wants_accommodation = args['<wants_accommodation>']

        if fellow:
            # add Fellow
            new_person = Fellow('%s %s' % (first_name, last_name))
            self.fellows.append(new_person)
            # then, allocate an office randomly, if available
            if self.offices:
                self.get_status_of_empty_offices()
                office_choice = random.choice(self.empty_offices)
                office_choice.occupants.append(new_person)
                self.fellows.append(new_person)
                self.allocated_fellows.append(new_person)
                self.allocated_people.append(new_person)
                print('Fellow %s %s has been successfully added' % (first_name, last_name))
                print('%s has been allocated the office %s' % (first_name, office_choice))
                if wants_accommodation:
                    self.get_status_of_empty_livingspaces()
                    livingspaces_choice = random.choice(self.empty_livingspaces)
                    livingspaces_choice.occupants.append(new_person)
                    print('%s has been allocated the office %s' % (first_name, livingspaces_choice))
            else:
                print('Sorry!!! There are no available offices at the moment. Try again!')
        else:
            if staff:
                # add staff
                new_person = Staff('%s %s' % (first_name, last_name))
                self.staff.append(new_person)
                # then allocate an Office randomly if available
                if self.offices:
                    self.get_status_of_empty_offices()
                    office_choice = random.choice(self.empty_offices)
                    office_choice.occupants.append(new_person)
                    self.staff.append(new_person)
                    self.allocated_staff.append(new_person)
                    self.allocated_people.append(new_person)
                    print('Staff %s %s has been successfully added' % (first_name, last_name))
                    print('%s has been allocated the office %s' % (first_name, office_choice))

        # Both Staff and Fellows must get accommodation
        # name = args['<first_name>'] + ' ' + args['<last_name>']
        # wants_accommodation = 'Yes' if args['<wants_accommodation>'] is 'Y' else 'No'
        # if wants_accommodation == 'N':
        #     if args['Staff']:
        #         new_person = Staff(name)
        #         self.staff.append(new_person)
        #     elif args['Fellow']:
        #         new_person = Fellow(name)
        #         self.fellows.append(new_person)
        # else:
        #     if self.offices:
        #         self.get_status_of_empty_rooms()
                # if not self.empty_offices:
                #     print('Sorry!! There are no empty offices at this time.')
                #     return
                # if args['Staff']:
                #     office_choice = random.choice(self.empty_offices)
                #     new_person = Staff(name)
                #     office_choice.occupants.append(new_person)
                #     self.staff.append(new_person)
                #     self.allocated_staff.append(new_person)
                #     print('Staff %s has been successfully added' % name)
                # elif args['Fellow']:
                #     office_choice = random.choice(self.empty_offices)
                #     new_person = Fellow(name)
                #     office_choice.occupants.append(new_person)
                #     self.fellows.append(new_person)
                #     self.allocated_fellows.append(new_person)
                #     print('Fellow %s has been successfully added' % name)
                #     self.allocated_people.append(new_person)
            # else:
            #     print('Sorry!!! There are no offices in the system.')
            #     return
            # self.people.append(new_person)
            # self.success_added_person(new_person, wants_accommodation)

    def get_status_of_empty_offices(self):
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


    def get_status_of_empty_livingspaces(self):
        for livingspace in self.livingspaces:
            if len(livingspace.occupants) < livingspace.capacity:
                if livingspace not in self.empty_livingspaces:
                    self.empty_livingspaces.append(livingspace)
                    self.empty_rooms.append(livingspace)
            elif len(livingspace.occupants) >= livingspace.capacity:
                if livingspace in self.empty_livingspaces:
                    self.empty_livingspaces.remove(livingspace)
                    self.empty_rooms.remove(livingspace)

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