"""
Usage:
    (dojo_app) create_room (livingspace|office) <room_name>...
    (dojo_app) add_person <first_name> <last_name> (Fellow|Staff) [<wants_accommodation>]
    (dojo_app) print_room <room_name>
    (dojo_app) print_allocations [--o=filename.txt]
    (dojo_app) print_unallocated [--o=filename.txt]
    (dojo_app)
    (dojo_app) (-i | --interactive)
    (dojo_app) (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app_plugins.docopt_extension import docopt_cmd
from app import my_dojo


class DojoApplication(cmd.Cmd):

    intro = "=============================================================\n" \
            "    WELCOME TO DOJO RANDOM ROOM ALLOCATION APPLICATION!\n" \
            "==============================================================\n\n" \
            "COMMANDS:\n\n" \
            "1. create_room (livingspace|office) <room_name>...\n" \
            "2. add_person <first_name> <last_name> (Fellow|Staff) [wants_accommodation]\n" \
            "3. print_room <room_name>\n" \
            "4. print_allocations [--o=filename.txt]\n" \
            "5. print_unallocated [--o=filename.txt]\n" \
            "6. reallocate_person <person_identifier> <new_room_name>\n" \
            "7. load_people <filename>\n"


    prompt = '(dojo_app)'
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (livingspace|office) <room_name>..."""
        my_dojo.create_room(args)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> (Fellow|Staff) [<wants_accommodation>]"""
        my_dojo.add_person(args)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        my_dojo.print_room(args)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [--o=filename.txt]"""
        my_dojo.print_allocations(args)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [--o=filename.txt]"""
        my_dojo.print_unallocated(args)

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        my_dojo.reallocate_person(args)

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people <filename>"""
        my_dojo.load_people(args)

    def do_quit(self, args):
        print('Good Bye!')
        exit()


options = docopt(__doc__, sys.argv[1:])
if options["--interactive"]:
    DojoApplication().cmdloop()

print(options)