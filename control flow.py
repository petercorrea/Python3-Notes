# Control Flow
if True:
    pass

elif "other value":
    pass

elif "other value":
    pass
else:
    pass

for num in range(0, 10):
    pass


while 3 > 6:
    pass

# Error Handling
try:
    for num in range(0, 5):
        pass
except:
    print("Must be a number")

if 5 > 10:
    raise ValueError("err...")

    #Enumerated Loops
to_turn_into_even = [1,3,5,7,9]

for index, var in enumerate(to_turn_into_even):
    var = var * 2
    print("Located at index ", index, "is", var)
