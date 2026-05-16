# DEFAULT VALUE FOR ATTRIBUTE
# and
# MODIFYING ATTRIBUTE VALUES

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # attribute with default value
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formated descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    # MODIFYING VALUE THROUGH METHOD 
    def uptade_odometer(self, mileage):
        """
        Set the odometer reading to the giving value.
        Reject the change if it attempts to oll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    # INCREMENTING VALUE THROUGH METHOD
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# default value

my_new_car.uptade_odometer(20)
my_new_car.read_odometer()
# modified through method

my_new_car.increment_odometer(5)
my_new_car.read_odometer()
# incremented through method

# MODIFYING VALUE DIRECTLY
my_new_car.odometer_reading = 30
my_new_car.read_odometer()
# modified directly

