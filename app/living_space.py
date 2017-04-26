from app.room import Room


class LivingSpace(Room):
    def __init__(self):
        super(LivingSpace, self).__init__()
        self.office = self.person

    def get_room_availability(self):
        pass