class Restaurant():
    def __init__(self, restaurantName, cuisineType):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        print("Restaurant name: " + self.restaurantName)
        print("Cuisine Type: " + self.cuisineType)

    def openRestaurant(self):
        print("The restaurant is open")

class User():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def describeUser(self):
        print("First name: " + self.firstName)
        print("Last name: " + self.lastName)

    def greetUser(self):
        print("Hi! ", self.firstName + " " + self.lastName)