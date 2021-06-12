groceries = [
    ["Baby Spinach", 2.78],
    ['Hot Chocolate', 3.70],
    ['Crackers', 2.10],
    ['Bacon', 9.00],
    ['Carrots', 0.56],
    ['Oranges', 3.08]
]
# print(groceries)
# print(groceries[1][1])
till = [
    ]
for item in range(len(groceries)):
    amount = input('how many items did you buy? ')
    amount2 = float(amount)
    line_1 = (groceries[item][0])
    line_2 = float(groceries[item][1])
    calc = (line_2 * amount2)
    print((line_1),calc)  
    till.append (calc)
#print(till)    
#subtotal = 
sum=sum(till)
print(f"Subtotal: ${sum}")

# https://medium.com/programminginpython-com/python-program-to-c
# alculate-the-sum-of-elements-in-a-list-ed2b80db8268

