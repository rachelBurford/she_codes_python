# boolean
is_raining = True
is_cold = True
#print(type(is_raining))
#print(type(is_cold))

#print(is_raining)
#print(not is_raining)
# print(is_raining) #true
# print(not is_raining) #false
# print(is_raining or is_cold) #true
# print(is_raining and not is_cold) #false
# print(is_raining or not is_cold) #true
# print(not is_raining and not is_cold) #false

# print(is_raining and is_cold)

#look at truth tables - resource

# temp = 16
# print(temp > 18)

# wind_chill = 3
# print(wind_chill > 4 )
# print(temp - wind_chill < 16)

# code = "free_ticket"
# print(code == "free_ticket")
# print(code != "free_ticket")

# is_raining = False
# if is_raining:
#     print("take an umbrella!")
# else:
#     print("No need for an umbrella")
# print("cats")

# temp = 16
# wind_chiill = 4

# if temp - wind_chiill < 16:
#     print("Take a jumper! Its a bit cool")
# elif temp - wind_chiill > 30:
#     print("its hot - stay home")
# else:
#     print("Wow - What a lovely day!")

# if temp < 16:
#     if is_raining:
#         print("just stay home!")
#     else:
#         print("weather ok today")
# else:
#     print("it's nice and warm today!")

# moths = 5

# moths_in_house = False
# mitch_is_home = True

# if moths_in_house:
#     if mitch_is_home:
#         print("Hooman! Help me get the moths")
#     else:
#         print("Meow .. Hiss Hiss")
# else:
#     if mitch_is_home:
#         print("climb on mitch")
#     else:
#         print("no threats detected.")

# light_colour = "Amber"
# car_detected = True

# #print(light_colour=="Red")

# if (light_colour =="Red"):
#     if car_detected:
#         print("flash!!")
#     else:
#         print("do nothing")
# else:
#     print("do nothing")

# height = input("how tall are you in cm's?")
# if (int(height)>120):
#     print("hop on!")
# else:
#     print("sorry eat more carrots! to grow tall")

# username = "fleur" 
# password = "PASSWORD123"

# if (username=="fleur" and password == "password123"):
#     print(f"Username : {username}")
#     print(f"Password : {password}")
#     print("Correct")
# else:
#     print(f"Username : {username}")
#     print(f"Password : {password}")
#     print("Incorrect!")

# email = input("enter your email")

# if "@" in email:
#     if "." in email:
#         print(f"{email}")
#         print("Email - Success!")
#     else:
#         print(f"{email}")
#         print("Email Error!")

# raining = True
# uv_index = 4
# tempreture = 23

# if (raining):
#     print("take an umbrealla")

# if (int(uv_index > 3)):
#     print("Wear sunscreen")

# if (tempreture < 20):
#     print("Take a Jumper!")

number1 = input("enter a number ")
number2 = input("enter another number ")
output1 = (float(number1) + float(number2))

if (output1 < 0):
    print("negative")
else:
    print("positive")