import csv

colours = []

with open("colours_20_simple.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

print(colours)
print()

col_chart = {}

for items in colours:
    print(f"{items[1]}: {items[2]}")
    col_chart [items[1]] = items[2]
print()
print(col_chart)
print(0)
for items,value in col_chart.items():
    print(f"{items}: {value}")