import csv
from datetime import date, datetime
from os import sep
from typing import Counter

turtles = []

with open("./data/2020_2021_turtle_data.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        turtles.append(line)

# print(turtles)
# print(turtles)

for lines in turtles[1:]:
#     # print(lines)
#     # print(lines[0])
#     # print(type(lines[0]))
    dated = lines[0]
    date = (datetime.strptime(dated, '%m/%d/%Y'))
    # print(x)
    monthed = (date.strftime("%B"))
    print(monthed)

    
    # print(type(monthed))

#     # turtles[lines] = monthed
#     # print(turtles)
#     # line[0] = 
#     # chilli_wishlist[1] = "carrot"
#     # # ^replace the list item in the 2nd posiion with >

dates = []
months = []

month = []
# for item in dates:
#     date = item
#     # print(date)
#     x = (datetime.strptime(date, '%m/%d/%Y'))
#     aus = (x.strftime("%d/%m/%Y"))
#     month.append(x.strftime("%B"))
# print(month)
# 
# # print(dates)
# print()
# for item,details in tur_chart.items():
#     name = (item)
#     print(datetime.strptime(dates, '%m/%d/%Y'))