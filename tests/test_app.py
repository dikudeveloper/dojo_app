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

    def test_create_room(self):
        # Office 'White', and Living Space 'Black' already exist in memory from setUp function
        # test single room creation
        self.assertEqual(1, len(self.test_my_dojo.offices))
        self.assertEqual(1, len(self.test_my_dojo.livingspaces))
        self.assertEqual(2, len(self.test_my_dojo.rooms))

        # Duplicate rooms not added to any list
        # """Create another test living space"""
        self.test_my_dojo.create_room({"<room_name>": ["Black"], "livingspace": True, "office": False})
        self.assertEqual(1, len(self.test_my_dojo.livingspaces))

        # Test many creation of many rooms
        self.test_my_dojo.create_room({"<room_name>": ['LivingBlack', 'LivingYellow'], "livingspace": True, "office": False})
        # Since we have added 2 more livingspaces to 1 former, we should have 3 now in the system
        self.assertEqual(3, len(self.test_my_dojo.livingspaces))

    # def test_add_person(self):
        self.assertEqual(1, len(self.test_my_dojo.fellows))
        self.assertEqual(1, len(self.test_my_dojo.staff))
        self.assertEqual(2, len(self.test_my_dojo.people))
        self.testfellow = self.test_my_dojo.people[0]
        self.teststaff = self.test_my_dojo.people[1]
