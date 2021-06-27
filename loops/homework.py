#participants = ["demo"]

# for students in range(5):
#     name = input("Add a Name: ")
#     participants.append(name)
# print(participants)
## runs the loop for 5 times then prints the statement
##rather then referencing the original range(len(list))

# tables = []

# entry = int(input("pick a number: "))

# for num in range(1,(entry + 1)):
#     calc = (entry * num)
#     tables.append((f"{entry} x {num} = {calc}"))
#     # (f"({entry} * 1 = {calc}))
#     print((f"{entry} x {num} = {calc}"))

# print(f"({entry} * {num}), 1 , 3)

# tbl = []

# entries = int(input("pick a number: "))

# for racoon in range(1,(entries +1)):

#     tbl.append(racoon)
# sum = sum(tbl)
# print(sum)
# # for number in range(input)

# random_num = []

# tab2 = []

# for item in random_num:
#     # print(item)
#     tab2.append(item)
# sum = sum(tab2)
# print(sum)

mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]
# below gets first letter of a list 
# for name in mailing_list:
#     print(name[0][0])

for name in range(len(mailing_list)):
    print(f"name  : {mailing_list[name][0]}") 
    print(f"email : {mailing_list[name][1]}")
    print()