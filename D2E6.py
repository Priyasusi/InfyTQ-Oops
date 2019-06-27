'''A vehicle is identified by its mileage (in kms per litre)
and fuel left (in litres) in the vehicle. From the fuel left, 5 litres will always be considered as reserve fuel.
At any point of time, the driver of the vehicle may want to know:
the maximum distance that can be covered without using the reserve fuel
how many kms he/she has already travelled based on the initial fuel the vehicle had
Write a Python program to implement the class chosen with its attributes and methods
based on the requirements given below:
identify_distance_that_can_be_travelled():
Return the distance that can be travelled by the vehicle without using the reserve fuel.
If the fuel left is less than or equal to reserve fuel, the method should return 0.
identify_distance_travelled(initial_fuel):
Return the distance so far travelled by the vehicle based on the initial fuel,fuel left and mileage.
Assume that initial fuel is always greater than fuel left.
Represent a vehicle and test your program by initializing the instance variables
and invoking the appropriate methods.'''
class Vehicle:
    def __init__(self):
        self.fuel_left=None
        self.mileage=None
    def identify_distance_that_can_be_travelled(self):
        if(self.fuel_left>5):
            return (self.fuel_left-5)*self.mileage
        else:
            return 0
    def identify_distance_travelled(self,initial_fuel):
        if(initial_fuel> self.fuel_left):
            return (initial_fuel-self.fuel_left)*self.mileage
        return self.mileage*self.fuel_left
   
v1=Vehicle()
v1.fuel_left=45
v1.mileage=50
print(v1.identify_distance_that_can_be_travelled())
print(v1.identify_distance_travelled(50))

