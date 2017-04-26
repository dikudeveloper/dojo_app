"""
Usage:
    (dojo_app) create_room (livingspace|office) <room_name>...
    (dojo_app) add_person <first_name> <last_name> <FELLOW> | <STAFF> [wants_accommodation]
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
# arguments = docopt(__doc__, version='Dojo Application')


class DojoApplication(cmd.Cmd):

    intro = "=============================================================\n" \
            "    WELCOME TO DOJO RANDOM ROOM ALLOCATION APPLICATION!\n" \
            "==============================================================\n\n" \
            "COMMANDS:\n\n" \
            "1. create_room (livingspace|office) <room_name>...\n" \
            "2. add_person <first_name> <last_name> <FELLOW> | <STAFF> [wants_accommodation]\n"

    prompt = '(dojo_app)'
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (livingspace|office) <room_name>..."""
        my_dojo.create_room(args)

    def do_quit(self, args):
        print('Good Bye!')
        exit()


options = docopt(__doc__, sys.argv[1:])
if options["--interactive"]:
    DojoApplication().cmdloop()

print(options)


# if __name__ == '__main__':
#     arguments = docopt(__doc__, version='Dojo Application')
#     print(arguments)
#     if arguments['create_room']:
#         print('create_room is dope')
#         dojoapp = DojoApplication()
#         # room_name = arguments['<room_name>']
#         # room_type = arguments['<room_type>']
#         # dojoapp.create_room(room_name, room_type)
#         dojoapp.create_room(arguments['<room_name>'])

