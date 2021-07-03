import csv
from datetime import date, datetime
from os import sep
from typing import Counter

turtles = []

with open("./data/2020_2021_turtle_data.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        turtles.append(line)


def convert_mmddyyyy_date(date):
    return datetime.strptime(date, '%m/%d/%Y')


def get_month_name(date):
    return date.strftime('%B')

# for item in turtles:
#     print(get_month_name(item[0]))

monthly = {}

for line in turtles:
    date = convert_mmddyyyy_date(line[0])


    for day in data:
        date = convert_mmddyyyy_date(day[0])
        month = get_month_name(date)
        monthly[month] = monthly[month] + [day[1:6]]
    for month in monthly.keys():
        days = monthly[month]
        nests = 0
        false_crawls = 0
        hit_rocks = 0
        hatched_nests = 0
        nest_pred = 0
        for day in days:
            nests += int(day[0])
            false_crawls += int(day[1])
            hit_rocks += int(day[2])
            hatched_nests += int(day[3])
            nest_pred += int(day[4])
        print([month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred])
    return [month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred]

# # print(turtles)

# # print(turtles)
# # months = {}
# # for lines in turtles[1:]:
# # #     # print(lines)
# # #     # print(lines[0])
# # #     # print(type(lines[0]))
# #     dated = lines[0]
# #     date = (datetime.strptime(dated, '%m/%d/%Y'))
# #     # print(x)
# #     monthed = (date.strftime("%B"))
# #     # print(monthed)
# #     # print(type(monthed))
# #     months.append(monthed)

# # print(type(months))

# # print(turtles)


# # for lines in turtles:
#     # print(months)
#     # print(type(months))
#     # print(type(monthed))

# # for line_item in turtles:
# #     turtles.insert(0,months)
# #     # txt1 = (f"{line_item[0]}")
# #     # time2 = txt1.replace("line one" , "line two")
# # print(turtles)
# # total_nests = {}

# # txt = "I like bananas"

# # x = txt.replace("bananas", "apples")

# # print(x)

# # ="".join(str(total_nests)[1:-1])
# # total_n= int(t_nests)

# #     # turtles[lines] = monthed
# #     # print(turtles)
# #     # line[0] = 
# #     # chilli_wishlist[1] = "carrot"
# #     # # ^replace the list item in the 2nd posiion with >

# # dates = []

# # month = []
# # for item in dates:
# #     date = item
# #     # print(date)
# #     x = (datetime.strptime(date, '%m/%d/%Y'))
# #     aus = (x.strftime("%d/%m/%Y"))
# #     month.append(x.strftime("%B"))
# # print(month)
# # 
# # # print(dates)
# # print()
# # for item,details in tur_chart.items():
# #     name = (item)
# #     print(datetime.strptime(dates, '%m/%d/%Y'))

