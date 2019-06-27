'''Write a python program to implement the created class diagram.
Represent bike rider and cycle rider, make them ride the respective vehicles.
Note: rides_vehicle(), rides_in_dome(), rides_blindfolded() methods should display appropriate messages. Assume that trained_status and
race_license are boolean variables and experience is an integer.'''
class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status=trained_status
        self.__experience=experience
    def rides_vehicle(self):
        pass
class CycleRider(Rider):
   def rides_blindfolded(self):
        pass
class BikeRider(Rider):
    def __init__(self,trained_status,experience,race_license):
        self.__race_license=race_license
        super().__init__(trained_status,experience)
    def rides_in_dome(self):
        pass


