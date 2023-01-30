products = [('diapers', 10.00), ('peanuts', 5.00), ('butter', 6.25), ('cheese', 3.00), ('milk', 3.5), 
('yogurt', 1.99), ('eggs', 4.5), ('bread', 4), ('shrimp', 2.5), ('coffee', 1.5)]

money = 50
menu = ('buy', 'return', 'quit')
cartlist = []

while menu != 'quit':
    for product in products:
        product_name = product[0].capitalize() 
        product_price = product[1] 
        print (f"{product_name} = {product_price}")
    menu = input("do you want to buy, return or quit?")

    if menu ==  'buy':
        item = input("what do you want to buy? ")
    elif menu  == 'return':
        item = input("what do you want to return? ")
else:
    print = ("thank you for visiting :) ")