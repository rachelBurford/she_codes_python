import csv

colour_chart = []

with open("colours_20_simple_v1.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colour_chart.append(line)

#print(colour_chart)

print(len(colour_chart))

for colours in colour_chart:
    print(f"{colours[0]}: {colours[1]}: {colours[2]}")
# i = 0 = 0
# while i=<(len(colour_chart)    

with open("colours_20_v2.csv", mode="w", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    for colour in colour_chart:
        writer.writerow([colour[2],f" Hex: {colour[1]}",f" RGB: {colour[0]}"])