groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers" : 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}
print(groceries)
#prints list of groceries
print(groceries["Baby Spinach"])
#references the first list item and then returns the second of the pair

groceries["Avocadoes"] = 1.00
#adds another to the overall list of items
print(groceries)

groceries["Hot Chocolate"] = 2.70
#replaces an item's pair value in a list
print(groceries)

del groceries["Crackers"]
#removes an item from the listing including its pair
print(groceries)

for item in groceries:
    print(item)
    #makes the key go in a singular line 
    print(f"{item}: ${groceries[item]}")
    #makes the key and value come out on same line
print()

for item, price in groceries.items():
    print(f"{item}: ${price}")
    #for key, value in list.keys():
    #print key ''' words '''value