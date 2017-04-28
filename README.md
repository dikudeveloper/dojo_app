# Synopsis
This is a Room Allocation System with a Command Line User Interface that was developed to Digitize and Randomize room allocation for one of Andela Kenya's facilities called the Dojo. When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only

# Usage
* create_room `<room_type> <room_name>`
* add_person `<person_name> <FELLOW | STAFF> [wants_accommodation]`
* print_room `<room_name>`
* print_allocations `[-o=filename]`
* print_unallocated `[-o=filename]`
* reallocate_person `<person_identifier> <new_room_name>`
* load_people
* save_state `[--db=sqlite_database]`
* load_state `<sqlite_database>`

# Motivation
This system will be used to automate the random allocation of spaces to Fellows and Staff at Andela Kenya's Dojo facility.

# Installation
To Install, make sure you have Python 3 installed, then run:
** pip install -r requirements.txt **
** python dojo_app.py -i **


