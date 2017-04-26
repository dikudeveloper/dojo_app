import unittest
from dojo_application import DojoApplication
from app.office import Office
from app.living_space import LivingSpace

from app.my_dojo import MyDojo
from app import my_dojo


class TestCreateRoom(unittest.TestCase):
    """Tests for the create_room command"""
    def setUp(self):
        self.test_dojo = MyDojo()

        """Create a test living space"""
        self.test_dojo.create_room({"<room_name>": ["Black"], "livingspace": True, "office": False})
        """Create a test office"""
        self.test_dojo.create_room({"<room_name>": ["White"], "livingspace": False, "office": True})

    def test_create_room(self):
        # Office 'White', and Living Space room 'Black' already exist in memory from setUp function
        # room creation
        self.assertEqual(1, len(self.test_dojo.offices))
        self.assertEqual(1, len(self.test_dojo.livingspaces))
        self.assertEqual(2, len(self.test_dojo.rooms))

        # Duplicate rooms not added to any list
        """Create a test living space"""
        self.test_dojo.create_room({"<room_name>": ["Black"], "livingspace": True, "office": False})
        self.assertEqual(1, len(self.test_dojo.livingspaces))

