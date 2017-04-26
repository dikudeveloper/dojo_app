import unittest
from main_app import MyInteractiveDojoApplication


class TestCreateRoom(unittest.TestCase):
    """Tests for create_room <room_type> <room_name>"""

    def setUp(self):
        self.my_dojo_app = MyInteractiveDojoApplication()

    def test_create_single_room_successfully(self):
        initial_room_count = len(self.my_dojo_app.all_rooms)
        blue_office = self.my_dojo_app.do_create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(self.my_dojo_app.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

