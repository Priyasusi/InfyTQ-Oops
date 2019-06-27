class InvalidMechanicSpecializationException(Exception):
    pass
class InvalidMechanicIdException(Exception):
    pass
    
class Mechanic:
    def __init__(self,mechanic_id,specialization,vehicle_count):
        self.__mechanic_id=mechanic_id
        self.__specialization=specialization
        self.__vehicle_count=vehicle_count
    def get_mechanic_id(self):
        return self.__mechanic_id
    def get_specialization(self):
        return self.__specialzation
    def get_vehicle_count(self):
        return self.__vehicle_count
    def set_mechanic_id(self,mechanic_id):
        self.__mechanic_id=mechanic_id
    def set_specialization(self,specialization):
        self.__specialization=specialization
    def set_vehicle_count(self,vehicle_count):
        self.__vehicle_count=vehicle_count
class VehicleService:
    def __init__(self,mechanic_list):
        self.__mechanic_list=mechanic_list
    def assign_vehicle_for_service(self,mechanic_id,vehicle_type):
        v_count=0
        try:
            if(mechanic_id in self.__mechanic_list):
                if(vehicle_type==Mechanic.get_specialization()):
                    v_count+=1
                    Mechanic.set_vehicle_count(v_count)
                else:
                    raise InvalidMechanicSpecializationException()
                    print("InvalidMechanicSpecializationException occured")
            else:
                raise InvalidMechanicIdException()
                print("InvalidMechanicIdException occured")    
        except Exception as e:
            print("Something went wrong:",str(e))
m1=Mechanic("106","TW",5)
vs1=VehicleService(["101","102","103","104","105"])
vs1.assign_vehicle_for_service("106","TW")

                




