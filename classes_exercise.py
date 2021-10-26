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
        """Returns vroom max_speed times."""

        print("vroom " * self.max_speed)

class Bus(Vehicle):
    """Represents a bus which is a type of vehicle.
    """

    def __init__(self):
        """Creates a bus  with a default capacity of 30."""

        # Call the superclass constructor

        super().__init__()

        self.capacity = 30

    def fare(self, age: float) -> None:
        """Prints the bus fare depending on the age of the rider."""

        # The fare cost varies depending on rider age.
        if age < 18 or age > 60:
            fare_cost = 0
        elif age >= 18 and age <= 60:
            fare_cost = 5

        # Print out the fare.
        print(f"The fare of the bus ride is ${fare_cost}.")

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