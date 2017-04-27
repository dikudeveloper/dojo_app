from app.room import Room


class Office(Room):
    capacity = 6
    office_count = []
    room_type = 'office'

    def __init__(self, name):
        """Initializes an Office Object"""
        self.name = name
        super(Office, self).__init__(self.name)

    def __repr__(self):
        """prints an Office Object"""
        return "<Office %s>" % self.name

    def __str__(self):
        return "%s" % self.name

