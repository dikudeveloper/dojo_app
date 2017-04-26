import unittest
from dojo_application import DojoApplication
from app.office import Office
from app.living_space import LivingSpace


class TestCreateRoom(unittest.TestCase):
    """Tests for the create_room command"""
    def setUp(self):
        self.dojo_app = DojoApplication()

    def test_create_room_office(self):
        self.assertEqual(self.dojo_app.create_room(self, 'office', 'Blue'), Office)

    def test_create_room_livingspace(self):
        self.assertEqual(self.dojo_app.create_room(self, 'livingspace', 'Blue'), LivingSpace)

    def test_create_room_multiple_office(self):
        self.assertEqual(
            self.dojo_app.create_room(self, 'office', 'Blue', 'Black', 'Red'), len(self.dojo_app.offices))

    def test_create_room_multiple_livingspace(self):
        self.assertEqual(
            self.dojo_app.create_room(self, 'livingspace', 'Blue', 'Black', 'Red'), len(self.dojo_app.livingspaces))