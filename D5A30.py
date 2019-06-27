class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
        
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
    def validate_quantity(self):
        if self.__quantity>=1 and self.__quantity<=5:
            return True
        return False
class Pizzaservice(Customer):
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__service_id=None
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.pizza_cost=None
        self.__additional_topping=additional_topping

    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return get_pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
    def validate_pizza_type(self):
        if self.__pizza_type.lower()=="small" or self.__pizza_type.lower()=="medium":
            return True
        return False
    def calculate_pizza_cost(self):
        
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            if self.__pizza_type.lower()=="small":
                cost=150
                Pizzaservice.counter+=1
                self.__service_id=str(self.__pizza_type[0])+str(Pizzaservice.counter)
                if self.__additional_topping:
                    topping_cost=35
                    self.pizza_cost=(topping_cost*self.__customer.get_quantity())+cost*self.__customer.get_quantity()
                else:
                    self.pizza_cost=cost*self.__customer.get_quantity()
                    print(self.pizza_cost)
                    
            elif self.__pizza_type.lower()=="medium":
                cost=200
                Pizzaservice.counter+=1
                self.__service_id=str(self.__pizza_type[0])+str(Pizzaservice.counter)
                if self.__additional_topping:
                    topping_cost=50
                    self.pizza_cost=topping_cost*self.__customer.get_quantity()+cost*self.__customer.get_quantity()
                else:
                    self.pizza_cost=cost*self.__customer.get_quantity()
        else:
            
            self.pizza_cost=-1
        return self.pizza_cost

class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.__distance_in_kms=distance_in_kms
        self.__delivery_charge=None
        super().__init__(customer,pizza_type,additional_topping)
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    def validate_distance_in_kms(self):
        if self.__distance_in_kms>=1 and self.__distance_in_kms<=10:
            #print(self.__distance_in_kms)
            return True
        return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            
            if self.pizza_cost !=-1:
                #a=super().calculate_pizza_cost()
                if self.__distance_in_kms<=5:
                    self.__delivery_charge=self.__distance_in_kms*5
                else:
                    dis=self.__distance_in_kms-5
                    self.__delivery_charge=25+dis*7
                self.pizza_cost=self.__delivery_charge+self.pizza_cost
                
        else:
            self.pizza_cost=-1

