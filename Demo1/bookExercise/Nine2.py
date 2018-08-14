from Nine import Restaurant, User

class IceCreamStand(Restaurant):
    def __init__(self,restaurantName, cuisineType, flavors):
        super().__init__(restaurantName, cuisineType)
        self.flavors = flavors


class Admin(User):
    def __init__(self, firstName, lastName, privileges):
        User.__init__(self,firstName, lastName)
        self.privileges = privileges

    def showPrivilege (self):
        print("The privilege is - " + self.privileges)

    def describeUser(self):
        print("This is admin")
        print("First name: " + self.firstName)
        print("Last name: " + self.lastName)

