#OOPR-Exer-13
#Start writing your code here
'''ABC DTH (Direct to Home) firm wants to calculate monthly rent for its
consumers. 35 min
A consumer can register for one Base Package.
Write a python program to implement the below given class diagram.
Class Description:
DirectToHomeService class:
Initialize static variable counter to 101
Inside constructor, auto-generate consumer_number starting from 101
BasePackage class:
validate_base_pack_name():
Validate base pack name. Valid values are "Silver", "Gold" and "Platinum".
If invalid, set attribute, base_pack_name as "Silver" and display "Base package name is incorrect, set to Silver"
calculate_monthly_rent():
Check if subscription period is between 1 and 24 (both inclusive). If so,
Validate base pack name
Identify monthly rent based on base pack. Refer table given.
Consumers are eligible for discount of one month's rent, if subscription period is more than 12 months
Calculate final monthly rent as per the formula given below:
final monthly rent = ((monthly rent * subscription period) – discount amount)/subscription period
Return the calculated final monthly rent
If not, return -1


Base Pack Name	Monthly Rent
Silver	350.00
Gold	440.00
Platinum	560.00 Note: Perform case sensitive string comparison  
For testing:
Create objects of BasePackage class
Invoke calculate_monthly_rent() on BasePackage object
Display the details'''


from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1
        self.__consumer_name=consumer_name
    def get_consumer_number(self):
        return self.__consumer_number
    def get_consumer_name(self):
        return self.__consumer_name
    @abstractmethod
    def calculate_monthly_rent(self):
        pass
class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period
        super().__init__(consumer_name)
    def get_base_pack_name(self):
        return self.__base_pack_name
    def get_subscription_period(self):
        return self.__subscription_period
    def validate_base_pack_name(self):
       bp_name=["Silver","Gold","Platinum"]
       if(self.__base_pack_name in bp_name):
            print("Base Pack Name is Valid")
       else:
            self.__base_pack_name="Silver"
            print("Base package name is incorrect, set to Silver")
    def calculate_monthly_rent(self):
        monthly_rent=0
        discount_amount=0
        final_monthly_rent=0
        if(self.__subscription_period>=1 and self.__subscription_period<=24):
            self.validate_base_pack_name()
            if(self.__base_pack_name=="Silver"):
                monthly_rent=350
                if(self.__subscription_period>12):
                    discount_amount=350
            elif(self.__base_pack_name=="Gold"):
                monthly_rent=440
                if(self.__subscription_period>12):
                    discount_amount=440
            elif(self.__base_pack_name=="Platinum"):
                monthly_rent=560
                if(self.__subscription_period>12):
                    discount_amount=560
                
            final_monthly_rent= ((monthly_rent *self.__subscription_period) - discount_amount)/self.__subscription_period
            return final_monthly_rent
        else:
            return -1
        
        

        
        
