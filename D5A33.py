class  OverdrawException(Exception):
    pass
class LimitReachedException(Exception):
    pass
class Account:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type=account_type
        self.__balance=balance
        self.__min_balance=min_balance
    def get_min_balance(self):
        return self.__min_balance
    def get_account_type(self):
        return self.__account_type
    def get_balance(self):
        return self.__balance
    def set_balance(self,min_balance):
        self.__balance=min_balance
        
class Customer(Account):
    def __init__(self,customer_id,customer_name,age,account):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__age=age
        self.__account=account
    
    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_age(self):
        return self.__age
    def get_account(self):
        return self.__account
    def withdraw(self,amount):
        try:
            if amount>self.__account.get_balance():
                raise OverdrawException
            else:
                
                if (self.__account.get_balance()-amount)<self.__account.get_min_balance():
                    
                    raise LimitReachedException
                else:
                    raise Exception
        except OverdrawException:
            print("Amount exceed the total balance")
            return 0
        except LimitReachedException:
            print("Amount almost reached the minimum balance")
            return 0
        except Exception:
            self.set_balance(self.__account.get_balance()-amount)
            return 1
    def take_card(self):
        print("Take card out from the ATM")
            
class PrivilegedCustomer(Customer):
    def __init__(self,customer_id,customer_name,age,account,bonus_point):
        super().__init__(customer_id,customer_name,age,account)
        self.__bonus_point=bonus_point
    def withdraw(self,amount):
        
        if super().withdraw(amount)==1:
            self.increase_bonus()
        else:
            print("Ensure that the card is taken out from the ATM")
        
    def get_bonus_point(self):
        return self.__bonus_point
    def increase_bonus(self):
        
        if super().get_account().get_balance()>1000:
            self.__bonus_point=10
        else:
            self.__bonus_point=2
        bonus=super().get_account().get_balance()+(super().get_account().get_balance()*self.__bonus_point/100)
        super().get_account().set_balance(bonus)
        
        
    
a1=Account("Savings",1000,500)
c1=Customer(100,"Gopal",43,acc)
pc1=PrivilegedCustomer(100,"Gopal",43,a1,10)
pc1.withdraw(400)



        

    
