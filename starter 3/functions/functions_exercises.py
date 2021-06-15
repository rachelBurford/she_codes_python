def convert_temp_f_to_d(temp_f):
    temp_d = (temp_f-32) * (5/9) 
    return round(temp_d,2)

print(convert_temp_f_to_d(32))
print(convert_temp_f_to_d(0))
print(convert_temp_f_to_d(350))

# boolean
is_raining = True
is_cold = True
#print(type(is_raining))
#print(type(is_cold))
