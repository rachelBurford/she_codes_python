import csv
from datetime import datetime
from os import sep
from typing import Counter

turtles = []

with open("./data/2020_2021_turtle_data.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        turtles.append(line)
# print(turtles)

dates = []
nests = []
crawls = []
rocks = []
hatched = []
disterbed = []
date_change = {
    "date":"month"
}
for line in turtles[1:]:
    # print(line)
    dates.append(line[0])
    nests.append(int(line[1]))
    crawls.append(int(line[2]))
    rocks.append(int(line[3]))
    hatched.append(int(line[4]))
    disterbed.append(int(line[5]))
     
# print(tur_chart)
# print(dates)
# print()
# for item,details in tur_chart.items():
#     name = (item)
#     print(datetime.strptime(dates, '%m/%d/%Y'))
month = []
# for item in dates:
#     date = item
#     # print(date)
#     x = (datetime.strptime(date, '%m/%d/%Y'))
#     aus = (x.strftime("%d/%m/%Y"))
#     month.append(x.strftime("%B"))
# print(month)

count_nests = sum(nests)
count_crawls = sum(crawls)
count_rocks = sum(rocks)
count_hatched = sum(hatched)
count_disterbed = sum(disterbed)
print("Overall")
print(f"Nests :{count_nests}")
print(f"Hatched : {count_hatched}")
print(f"Crawls : {count_crawls}")
print(f"Rocks : {count_rocks}")
print(f"Nest Predation :{count_disterbed}")
# print(date_change)
# for items in month:
#     turtles.insert(-1,[items])
#     print(turtles)
#     print(f"{date} = {month}")
# # print(month)
#     for line in turtles:
#         print(f" us date ={line[0]} nests:{line[1]}, false crawsl:{line[2]}, hit Rocks:{line[3]}, hatched:{line[4]}, Nest Predation:{line[5]}")

# Date Collected', 'Nests', 'Total No. False Crawls', 'Hit Rocks', 'Hatched Nests', 'Nest predation'



action_counts = {
    "Nests":0,
    "Total No. False Crawls":0,
    "Hit Rocks":0,
    "Hatched Nests":0,
    "Nest predation":0,
}

