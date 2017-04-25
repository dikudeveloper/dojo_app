import unittest
from app.room import Room


class TestCreateRoom(unittest.TestCase):
    """Tests for create_room <room_type> <room_name>
    create_room <room_type> <room_name> creates rooms in the Dojo. Using this command, the user should be able
    to create as many rooms as possible by specifying multiple room names after the create_room command.
    """

    def setUp(self):
        room_object = Room()

    def test_create_room_successfully(self):
        pass