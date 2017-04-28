from app.person import Person

# Fellow class
# Creates a Staff object that inherits from Person class


class Staff(Person):
    person_type = 'Staff'

    def __init__(self, name):
        super(Staff, self).__init__(name)

    def __repr__(self):
        return "<Staff %s>" % self.name

    def __str__(self):
        return "%s" % self.name
