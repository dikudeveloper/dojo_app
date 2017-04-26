from app.room import Room


class LivingSpace(Room):
    capacity = 4

    def __init__(self, name):
        self.name = name
        super(LivingSpace, self).__init__(self.name)

    def __repr__(self):
        return "<LivingSpace %s>" % self.name

    def __str__(self):
        return "%s" % self.name

