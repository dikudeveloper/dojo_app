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
                print('Room %s that you tried to create already exists in the Dojo!' % room_name)
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
            self.people.append(new_person)
            # then, allocate an office randomly, if available
            if self.offices:
                self.get_status_of_empty_offices()
                if len(self.empty_offices) > 0:
                    office_choice = random.choice(self.empty_offices)
                    office_choice.occupants.append(new_person)
                    # self.fellows.append(new_person)
                    self.allocated_fellows.append(new_person)
                    self.allocated_people.append(new_person)
                    print('Fellow %s %s has been successfully added' % (first_name, last_name))
                    print('%s has been allocated the office %s' % (first_name, office_choice))

                    if wants_accommodation == 'Y':
                        self.get_status_of_empty_livingspaces()
                        if len(self.empty_livingspaces) > 0:
                            livingspaces_choice = random.choice(self.empty_livingspaces)
                            livingspaces_choice.occupants.append(new_person)
                            print('%s has been allocated the livingspace %s' % (first_name, livingspaces_choice))
                        else:
                            print('There are no LivingSpaces at the moment! Create a LivingSpace using \'create_room\'')
                else:
                    print('Sorry!!! There are no vacant spaces in the available offices at the moment. '
                          'Please create a new office using \'create_room\' command!')
            else:
                print('NO OFFICES! Please create an Office and retry!')
        else:
            if staff:
                # add staff
                new_person = Staff('%s %s' % (first_name, last_name))
                self.staff.append(new_person)
                self.people.append(new_person)
                # then allocate an Office randomly if available
                if self.offices:
                    self.get_status_of_empty_offices()
                    if len(self.empty_offices) > 0:
                        office_choice = random.choice(self.empty_offices)
                        office_choice.occupants.append(new_person)
                        # self.staff.append(new_person)
                        self.allocated_staff.append(new_person)
                        self.allocated_people.append(new_person)
                        print('Staff %s %s has been successfully added' % (first_name, last_name))
                        print('%s has been allocated the office %s' % (first_name, office_choice))
                    else:
                        print('Sorry!!! There are no vacant spaces in the available offices at the moment. '
                              'Please create a new office using \'create_room\' command!')

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

    def print_room(self, args):
        """Print the names of all the people in room_name on the screen"""
        room_name = args["<room_name>"]
        if room_name not in [room.name for room in self.rooms]:
            print("Sorry!! The room you have entered does not exist. Try creating it with \'create_room\' command")
            return
        for room in self.rooms:
            if room.name == room_name:
                if room.occupants:
                    for person in room.occupants:
                        print('Room %s: %s' % (room.name, person.name))
                else:
                    print("This room has no occupants.")

    def print_allocations(self, args):
        """Prints a list of allocations onto the screen.
        Specifying the optional -o option outputs the registered allocations to a text file
        """
        if len(self.rooms) == 0:
            print('The Dojo has NO Rooms. Please create rooms using \'create_room\'')
        else:
            print_output = ''
            for room in self.rooms:
                print_output += room.name + '\n'
                print_output += '-' * 30 + '\n'
                if room.occupants:
                    print_output += ','.join([person.name for person in room.occupants]) + '\n\n'
                else:
                    print_output += 'NO OCCUPANTS IN THIS ROOM!.\n'
            if args['--o']:
                # Open 'filename' in mode wt and return file object, f
                with open(args['--o'], 'wt') as f:
                    f.write(print_output)
                    print('OUTPUT OF PRINT ALLOCATIONS HAS BEEN SAVED TO FILE: %s' % (args['--o']))
            else:
                print(print_output)

    def print_unallocated(self, args):
        """Prints a list of allocations onto the screen.
        Specifying the optional -o option outputs the registered allocations to a text file
        """
        if len(self.rooms) == 0:
            print('The Dojo has NO Rooms. Please create rooms using \'create_room\'')
        else:
            print_output = ''
            if len(self.people) > 0:
                for person in self.people:
                    # Get unallocated people
                    if person not in self.allocated_people:
                        print_output += person.name + "\n"
                    # Populate unallocated_people list
                    # if person not in self.unallocated_people:
                    #     self.unallocated_people.append(person)
                if args['--o']:
                    # Open 'filename' in mode wt and return file object, f
                    with open(args['--o'], 'wt') as f:
                        f.write(print_output)
                        print('OUTPUT OF PRINT ALLOCATIONS HAS BEEN SAVED TO FILE: %s' % (args['--o']))
                else:
                    print(print_output)
            else:
                print('NO PEOPLE IN THE SYSTEM!!')
