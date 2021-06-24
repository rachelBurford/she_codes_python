from typing import Counter


# names = [
#     "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
#     "Joy", "Katie", "Maddie", "Tash", "Nic",
#     "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
#     "Viv", "Anna", "Catherine", "Catherine", "Debby",
#     "Gab", "Megan", "Michelle", "Nic", "Roxy",
#     "Samara", "Sasha", "Sophie", "Teagen", "Viv"
# ]

names = [
    "Miranda", "Sophie", "Emily", "Taylor", "Anne",
    "Djuarli", "Anika", "Rosie", "Miranda", "Taylor",
    "Abby", "Sarah", "Teagen", "Abby", "Abby",
    "Maddie", "Miranda", "Rosie"
]

name_list = Counter(names)

print(name_list)

for key,value in name_list.items():
    print(key,value)