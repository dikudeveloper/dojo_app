"""
Usage:
    dojo_app create_room <room_type> <room_name>
    dojo_app add_person <person_name> <FELLOW | STAFF> [wants_accommodation]
    dojo_app print_room <room_name>
    dojo_app print_allocations [-o=filename]
    dojo_app print_unallocated [-o=filename]
    dojo_app reallocate_person <person_identifier> <new_room_name>
    dojo_app load_people
    dojo_app save_state [--db=sqlite_database]
    dojo_app load_state <sqlite_database>
    dojo_app
    dojo_app (-i | --interactive)
    dojo_app (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt
from app_plugins.docopt_extension import docopt_cmd


class MyInteractiveDojoApplication(cmd.Cmd):
    """Randomize room allocation for The Dojo"""

    # A string to issue as an intro or banner (Cmd.intro)
    intro = '=================================================\n' \
            '   WELCOME TO MY DOJO INTERACTIVE APPLICATION!   \n' \
            '=================================================='
    # The prompt issued to solicit input from the user (Cmd.prompt)
    prompt = '(dojo_app) '

    def __init__(self):
        super(MyInteractiveDojoApplication, self).__init__()
        self.all_rooms = []
        self.vacant_rooms = []
        self.offices = []
        self.vacant_offices = []
        self.living_spaces = []
        self.vacant_living_spaces = []
        self.people = []
        self.unallocated_people = []
        self.allocated_people = []
        self.fellows = []
        self.allocated_fellows = []
        self.staff = []
        self.allocated_staff = []

    @docopt_cmd
    def do_create_room(self, *arg):
        """Usage: create_room <room_type> <room_name>"""

        print(*arg)

    def do_quit(self, arg):
        """Quits Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        MyInteractiveDojoApplication().cmdloop()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass
