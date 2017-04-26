from app.person import Person

# Fellow class
# Creates a Fellow object that inherits from Person class


class Fellow(Person):
    person_type = 'Fellow'

    def __init__(self, name):
        super(Fellow, self).__init__(name)

    def __repr__(self):
        return "<Fellow %s>" % self.name
