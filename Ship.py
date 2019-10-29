# This code was made because yolo by a crazy guy during his free time 
# Names used in the code is random and is not intended to target any specific individual

# create ships
class Ship:
    def __init__(self, name):
        self.name = name

        # list of passengers in a ship
        self.passengers = []

    # to board passengers into the ship
    def fillShip(self, person):
        self.passengers.append(person)

    # prints the name of persons on the ship
    def showPassengers(self):
        print(self.passengers)


# create person to put in a ship
class Person:
    def __init__(self, name):
        self.name = name

    # just like __init__, __repr__ is automatically called when the object is
    # created. Here, it returns self.name as a string representation of the
    # object. When calling print(person_object), it will print the name of the
    # person instead of it's memory location
    def __repr__(self):
        return self.name

    def destroy(self):
        del self


# create a ship named Titanic
titanic = Ship("Titanic")

# create a person named Laurent
laurent = Person("Laurent")
# create a person named Henusha
henu = Person("Henusha")
# create a person named neko(which is not really a person actually)
third_wheeler = Person("neko")

# adds Laurent on the Titanic
titanic.fillShip(laurent)
# adds Henusha on the Titanic
titanic.fillShip(henu)


print("Passengers currently on the Titanic: ", end="")
titanic.showPassengers()

# just to print a blank line
print()

# adds neko to the titanic
titanic.fillShip(third_wheeler)
print("A cat has jumped onto the Titanic")
print("Passengers currently on the Titanic: ", end="")
titanic.showPassengers()


# 
# destroys the poor little cute kitty :<
third_wheeler.destroy()


titanic.showPassengers()
print()