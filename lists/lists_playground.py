chilli_wishlist = [
     "igloo",
     "chicken",
     "donut toy",
     "cardboard box"
 ]
# print(chilli_wishlist)
# # ^ print the list
# print(len(chilli_wishlist))
# # ^ print the number of items in the list
# print(chilli_wishlist[-1])
# # ^ Print the item in the last position 
# print(chilli_wishlist[0:2])
# # Print the item in the 0 and 1 position 
# # ( inclusive of the first but upto the last)
# chilli_wishlist[1] = "carrot"
# # ^replace the list item in the 2nd posiion with >
# print(chilli_wishlist)
# # reprint the list to see changes

#print(chilli_wishlist[2:4])
#print a list with 2 and 3 positions

#chilli_wishlist.append("dig mat")
#apped adds to the end
#print(chilli_wishlist)

#chilli_wishlist.append(["kong","tennis ball","tower","hat"])
# append add a new list of things at the end - as a single item
#print(chilli_wishlist)
#chilli_wishlist.extend(["sunny days","milk drinks","watching tv"])
# adds the new list - use for two list together 
# print(chilli_wishlist)

# print(chilli_wishlist.pop(2))
# #removes last item if blank or place items displays place item in words

# print(chilli_wishlist)

# chilli_wishlist.insert(-2,"napping!!")
# print(chilli_wishlist)

# chilli_wishlist.pop(2)
# print(chilli_wishlist)

# # Add a new item to position -2
# chilli_wishlist.insert(-2, "bone")
# print(chilli_wishlist)
# # Remove the third item from the list
# chilli_wishlist.pop(2)
# print(chilli_wishlist)
# # Add four new items to the end of the list.
# chilli_wishlist.extend(["treats", "milk sticks", "bird", "will"])
# # Remove the "igloo" item from the list.
# chilli_wishlist.remove("igloo")
# print(chilli_wishlist)

print()

# lists inside lists

chilli_wishlist = [
["igloo"], #bed
["donut toy","tennis ball","crocidile"], #toys
["chicken", "peanut butter"], # treats
    ["cardboard box", "kong"] # puzzles
]
print(chilli_wishlist)
print(chilli_wishlist[0][0])

print()

print(chilli_wishlist[3][0])