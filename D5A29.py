#OOPR-Assgn-29
#Start writing your code here
from abc import ABCMeta,abstractmethod
class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.bill_amount=None
        self.bill_id=None
    
    def get_customer_name(self):
        return self.__customer_name
        
    @abstractmethod
    def calculate_bill_amount(self):
        pass
class OccasionalCustomer(Customer):
    __counter=1000 
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms=distance_in_kms
        OccasionalCustomer.__counter+=1
        self.bill_id="O"+str(OccasionalCustomer.__counter)
    def validate_distance_in_kms(self):
        if(self.__distance_in_kms>=1 and self.__distance_in_kms<=5):
            return True
        else:
            return False
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    def calculate_bill_amount(self):
        if(self.validate_distance_in_kms()):
            no_of_tiffin=1
            cost_per_tiffin=50
            del_charge=0
            distance=self.get_distance_in_kms()
            if(distance>=1 and distance<=2):
                del_charge=5*distance
            elif(distance>2 and distance<=5):
                del_charge=7.5*distance
            self.bill_amount=cost_per_tiffin+del_charge
            
        else:
            self.bill_amount=-1
        return self.bill_amount
   
class RegularCustomer(Customer):
    __counter=100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin=no_of_tiffin
        RegularCustomer.__counter+=1
        self.bill_id="R"+str(RegularCustomer.__counter)
    def validate_no_of_tiffin(self):
        if(self.__no_of_tiffin>=1 and self.__no_of_tiffin<=7):
            return True
        else:
            return False
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
    def calculate_bill_amount(self):
        cost_per_tiffin=50
        no_of_days=7
        if(self.validate_no_of_tiffin()):
           self.bill_amount=self.__no_of_tiffin*cost_per_tiffin* no_of_days
        else:
            self.bill_amount=-1
        return self.bill_amount
    

        

        
        
