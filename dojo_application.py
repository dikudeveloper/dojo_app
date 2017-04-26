"""
Usage:
    dojo_app create_room <room_type> <room_name>...
    dojo_app add_person <first_name> <last_name> <FELLOW> | <STAFF> [wants_accommodation]
    dojo_app
    dojo_app (-i | --interactive)
    dojo_app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Dojo Application')
    print(arguments)


# class DojoApplication(object):
#
#     def __init__(self):
#         self.all_rooms = []
#         self.vacant_rooms = []
#         self.offices = []
#         self.vacant_offices = []
#         self.living_spaces = []
#         self.vacant_living_spaces = []
#         self.people = []
#         self.unallocated_people = []
#         self.allocated_people = []
#         self.fellows = []
#         self.allocated_fellows = []
#         self.staff = []
#         self.allocated_staff = []
#
#     def create_room(self):
#         pass