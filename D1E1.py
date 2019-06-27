'''#OOPR-Exer-1
A better solution would be to modularize the code and separate the logic for
Mobiles and Shoes.
Modify the code as per the below guidelines:
Create two functions: purchase_mobile and purchase_shoe
purchase_mobile() takes two parameters: price and brand
purchase_shoe() takes two parameters: price and material
If the mobile brand is “Apple”, discount is 10%, else discount is 5%
If the shoe material is “leather”, tax is 5%, else tax is 2%'''
                                                       
def purchase_shoe(price,material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    print("Total price of "+material+" shoe is "+str(total_price))
def purchase_mobile(price,brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print("Total price of "+brand +" mobile is "+str(total_price))
purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")

