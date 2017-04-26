from app.room import Room


class Office(Room):
    def __init__(self):
        super(Office, self).__init__()
        self.office = self.person

    def get_room_availability(self):
        pass