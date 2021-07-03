import csv
import datetime
from os import sep
# from typing import Counter

turtles = []

with open("./data/2020_2021_turtle_data.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        turtles.append(line)
# print(turtles)

dates = []

for stacks in turtles[1:]:
    # print(f"date: {stacks[0]}: nests:{stacks[1]}")
    
    name = str(stacks[0])
    two = str(stacks[1])
    three = str(stacks[2])
    seperated_name = name.split("/")
    dates.append(seperated_name)
    for n in seperated_name:
        print(n)
        # y = datetime.datetime(int(n))
        # print(y)
    # print(seperated_name)
# print(dates)
# for cards in dates[1:]:
    # print(cards)
    # aud_date = (f"{cards[1]}/{cards[0]}/{cards[2]}")
    
x = datetime.datetime.now()
# print(x.strftime("%A"))



# import csv as pd
# df = pd.DataFrame({
#     'date': [str()]
# })

# for stacks in turtles:
    # print(aud_date,two,three)

# with open("new_turtle_data.csv", mode="w", encoding="utf-8") as csv_file:
#     writer = csv.writer(csv_file, delimiter=",")
#     for stacks in turtles:
#         writer.writerow([])



    # print(seperated_name)
    # print()
    # print(name)
    # print(two)
    # print(three)   
#     print(f"{seperated_name}")
# print(type(seperated_name))
# print(seperated_name)
#     print(name)
# print(seperated_name)
    # for logs in seperated_name:
    #     print(logs)
    # print(type(logs))
    # print(f"{logs[0]}/{logs[1]}/{logs[2]}")