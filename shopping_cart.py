# shopping_cart.py

from pprint import pprint


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# INFO CAPTURE / INPUT PROCESS

total_price = 0

while True:
    selected_id = input("Please input a product identifier:") 
    #  print(type(selected_id)) 
    #  Note: if you enter 9, the result is "9" as a (string) output.

    if selected_id == "DONE":
        break
    else:
        matching_products = [item for item in products if int(item["id"]) == int(selected_id)] #List info: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/datatypes/lists.md

        matching_product = matching_products[0]

        for item in products:    
            price_usd = to_usd(item['price'])
        total_price = total_price + matching_product["price"]
        print("SELECTED PRODUCT:",matching_product["name"],to_usd(matching_product["price"]))



# INFO DISPLAY / OUTPUT PROCESS

print("TOTAL PRICE:",to_usd(total_price))



# TO DO
# Write a program that asks the user to input one or more product identifiers, then looks up the prices for each, then prints an itemized customer receipt including the total amount owed.# 
# The program should use one of the provided datastores (see "Data Setup") to represent the store owner's inventory of products and prices.# 
# The program should prompt the checkout clerk to input the identifier of each shopping cart item, one at a time.# 
# When the clerk inputs a product identifier, the program should validate it, displaying a helpful message like "Hey, are you sure that product identifier is correct? Please try again!" if there are no products matching the given identifier.# 
# At any time the clerk should be able to indicate there are no more shopping cart items by inputting the word DONE or otherwise indicating they are done with the process.# 
# After the clerk indicates there are no more items, the program should print a custom receipt on the screen. The receipt should include the following components:# 
#    A grocery store name of your choice
#    A grocery store phone number and/or website URL and/or address of choice
#    The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
#    The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
#    The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
#    The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
#    The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
#    A friendly message thanking the customer and/or encouraging the customer to shop again
#    The program should be able to process multiple shopping cart items of the same kind, but need not display any groupings or aggregations of those items (although it may optionally do so).

# Project submissions will be evaluated according to the requirements set forth above, as summarized by the rubric below:
# Category	Requirement	Weight
# Info Inputs	Captures / scans product identifiers	10%
# Info Inputs	Handles invalid inputs	10%
# Info Inputs	Handles the "DONE" signal	10%
# Info Outputs (Receipt)	Displays store info	10%
# Info Outputs (Receipt)	Displays checkout date and time	10%
# Info Outputs (Receipt)	Displays names and prices of all scanned products	15%
# Info Outputs (Receipt)	Displays tax and totals	15%
# Dev Process	Submitted via Git repository which reflects an incremental revision history	20%
# END