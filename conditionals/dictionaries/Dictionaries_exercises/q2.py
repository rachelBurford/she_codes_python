from typing import Counter


colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}


colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

colours2 = [
    "orange",
    "purple",
    "blue",
    "yellow",
    "green",
    "green",
    "purple",
    "purple",
    "green",
    "blue",
    "green",
    "orange",
    "purple",
    "blue",
    "green",
    "orange",
    "orange",
    "red",
    "yellow",
    "yellow"
]

my_count = Counter(colours)
my_count2 = Counter(colours2)

# print(my_count)
print()

for key,count in my_count.items():
    colour_counts [key] = count
# print(colour_counts)
# print()
for key,count in colour_counts.items():
   print(f"{key}: {count}")
print()

for key,blob in my_count2.items():
    colour_counts [key] = blob
# print(colour_counts)
for key,blob in colour_counts.items():
    print(f"{key}: {blob}")