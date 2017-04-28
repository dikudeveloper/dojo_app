import unittest
from app.office import Office
from app.room import Room
from app.living_space import LivingSpace

from app.my_dojo import MyDojo


class TestMyDojo(unittest.TestCase):
    """Tests for the create_room command"""
    def setUp(self):
        self.test_my_dojo = MyDojo()

        # Create a test living space
        self.test_my_dojo.create_room({"<room_name>": ["LivingBlack"], "livingspace": True, "office": False})
        # Create a test office
        self.test_my_dojo.create_room({"<room_name>": ["OfficeWhite"], "livingspace": False, "office": True})
        # Create a test person, Fellow who wants accommodation
        self.test_my_dojo.add_person({'<first_name>': 'Joseph', '<last_name>': 'Diku',
                                      '<wants_accommodation>': 'Y', 'Fellow': True, 'Staff': False})
        # Create a test person, Staff, who wants accommodation
        self.test_my_dojo.add_person({'<first_name>': 'Master', '<last_name>': 'Chan',
                                      '<wants_accommodation>': 'Y', 'Fellow': False, 'Staff': True})

    def test_create_single_room_office(self):
        # Office 'White' exists in memory from setUp function
        self.assertEqual(1, len(self.test_my_dojo.offices))

    def test_create_single_room_livingspace(self):
        # LivingSpace 'Black' exists in memory from setUp function
        self.assertEqual(1, len(self.test_my_dojo.livingspaces))

    def test_total_number_of_rooms_created(self):
        # two rooms exist in memory from setUp function
        self.assertEqual(2, len(self.test_my_dojo.rooms))

    def test_duplicate_rooms_not_created(self):
        # Create another test living space room with name 'LivingBlack' as before and test that count is still 1
        # Joseph (Fellow wanted_accommodation), and now we create another Living Space room called 'LivingBlack'
        self.test_my_dojo.create_room({"<room_name>": ["LivingBlack"], "livingspace": True, "office": False})
        self.assertEqual(1, len(self.test_my_dojo.livingspaces))

    def test_create_multiple_rooms(self):
        # Create 2 other LivingSpace rooms;
        self.test_my_dojo.create_room({"<room_name>": ['LivingRed', 'LivingYellow'], "livingspace": True, "office": False})
        # Since we have added 2 new livingspaces to 1 former, there are now 3 LivingSpaces in the Dojo
        self.assertEqual(3, len(self.test_my_dojo.livingspaces))

    def test_add_fellow(self):
        self.assertEqual(1, len(self.test_my_dojo.fellows))

    def test_add_staff(self):
        self.assertEqual(1, len(self.test_my_dojo.staff))

    def test_total_number_of_people_added(self):
        self.assertEqual(2, len(self.test_my_dojo.allocated_people))

    def test_add_fellow_with_accommodation(self):
        self.test_my_dojo.add_person({'<first_name>': 'Ben', '<last_name>': 'WWW',
                                      '<wants_accommodation>': 'Y', 'Fellow': True, 'Staff': False})
        # at this point, there were 2 occupants in the only office created so far, 'OfficeWhite'; 1 more is added
        # at this point, the total capacity of all livingspaces should be 12 (3 livingspaces * 4 occupants)
        self.assertEqual(3, len(self.test_my_dojo.offices[0].occupants))

    def test_add_staff_with_accommodation(self):
        self.test_my_dojo.add_person({'<first_name>': 'Mark', '<last_name>': 'Zuckerberg',
                                      '<wants_accommodation>': 'Y', 'Fellow': False, 'Staff': True})
        # at this point, there were 3 occupants in the only Office created; and total LivingSpaces is 1
        self.assertEqual(3, len(self.test_my_dojo.offices[0].occupants))
        self.assertEqual(1, len(self.test_my_dojo.livingspaces))

    def test_load_people_from_input_file(self):
        # Create a new office to store more people from an input text file"""
        self.test_my_dojo.create_room({'<room_name>': ['Office123'], 'livingspace': False, 'office': True})
        # Load 7 new people from input_file.txt text file
        self.test_my_dojo.load_people({'<filename>': 'tests\load_people_test_input_file.txt'})
        # Dojo app should now have people (especially in offices because each person gets an office)
        self.assertEqual(9, len(self.test_my_dojo.people))











