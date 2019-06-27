'''Assignment 3:
Implement the Customer class based on the identified class structure and details given below:

    1. Consider all instance variables and methods to be public
    2. Assume that bill_amount is initialized with total bill amount of the customer
    3. Customer is eligible for 5% discount on the bill amount
    4. purchases(): Compute discounted bill amount and pay bill
    5. pays_bill(amount): Display, <customer_name> pays bill amount of Rs. <amount>

Represent few customers, invoke purchases() method and display the details.


Note: Verification is done only for the class structure.'''
class Customer:
    def __init__(self):
        self.customer_name=None
        self.bill_amount=None
    def purchases(self):
        self.bill_amount-=self.bill_amount*(5/100)
        self.pays_bill(self.bill_amount)
    def pays_bill(self,amount):
        print(self.customer_name+" pays bill amount of Rs."+str(self.bill_amount))
c1=Customer()
c1.customer_name="Priya"
c1.bill_amount=500
c1.purchases()

