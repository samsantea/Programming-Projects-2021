# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times - if max_speed 60, say vroom 60 times wow
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""

# Your code goes under here

class Vehicle:
    """Represents a vehicle.

    Attributes:
        name: The name of the vehicle.
        max_speed: The maximum speed the vehicle can go at.
        capacity: The amount of persons that can sit inside of the vehicle safely.
    """

    def __init__(self):
        """Initializes a new vehicle with default values."""

        self.name = "Lambo"
        self.max_speed = 100
        self.capacity = 4

    def vroom(self):
        """Vehicle goes vroom multiplied by the
        amount of speed times."""

        print("vroom " * self.max_speed)

class Bus(Vehicle):
    """Represents a bus that can drive
    humans around in it"""

    def fare(self, age: float = 18) -> None:
        """Tells how much fare is for a particular age."""

        # The fare cost varies depending on rider age.
        if 18 <= age <= 60:
            print(f"The fare of the bus ride is $5.00. 🚌")
        else:
            print("You ride free! 🚌")
        # Print out the fare.


blue_car = Vehicle()
print(blue_car.name)
blue_car.name = "Optimus"
blue_car.max_speed = 120
print(blue_car.name)
print(blue_car.max_speed)
print(blue_car.capacity)

blue_car.vroom()

yellow_bus = Bus()
yellow_bus.name = "Bumblebee"
yellow_bus.max_speed = 80

print(yellow_bus.name)
print(yellow_bus.max_speed)
print(yellow_bus.capacity)

yellow_bus.fare(15)
yellow_bus.fare(25)
yellow_bus.fare(90)

# Mr. Ubial's example

a_vehicle = Vehicle()
a_vehicle.name = "Le Ferrari"
a_vehicle.max_speed = 372
a_vehicle.capacity = 2
a_vehicle.vroom()

a_bus = Bus()
a_bus.name = "TransLink Bus - 407"
a_bus.capacity = 35
a_bus.max_speed =  140
a_bus.vroom()
a_bus.fare(-1)
a_bus.fare(0)
a_bus.fare(17)
a_bus.fare(18)
a_bus.fare(60)
a_bus.fare(61)