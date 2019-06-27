'''Assignment 5:
Write a Python program to implement the class chosen with its attributes and methods.
Note:
Consider all instance variables to be private and methods to be public
Include getter and setter methods for all instance variables
Display appropriate error message, if the vehicle type is invalid
Perform case sensitive string comparison
Represent few objects of the class, initialize instance variables using setter methods,
invoke appropriate methods and test your program.'''
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_cost=None
        self.__vehicle_type=None
        self.__premium_amount=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount
    def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            self.__premium_amount=self.__vehicle_cost*(2/100)
        elif(self.__vehicle_type=="Four Wheeler"):
            self.__premium_amount=self.__vehicle_cost*(6/100)
        else:
            print("Invalid Vehicle Type")
           
    def display_vehicle_details(self):
        print(self.__vehicle_id)
        print(self.__vehicle_cost)
        if(self.__vehicle_type=="Two Wheeler" or self.__vehicle_type=="Four Wheeler"):
            print(self.__vehicle_type)
        else:
            print("Invalid Vehicle Type")
            
        print(self.__premium_amount)
v1=Vehicle()
v1.set_vehicle_id(1)
v1.get_vehicle_id()
v1.set_vehicle_cost(50000)
v1.get_vehicle_cost()
v1.set_vehicle_type("Two Wheeler")
v1.get_vehicle_type()
v1.calculate_premium()
v1.display_vehicle_details()

    
        
