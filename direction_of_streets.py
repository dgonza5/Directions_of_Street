"""
Start by getting the street number

If the street number is even, display eastbound

If it is not even, display westbound

Finish program
"""


def calculate_street(street):
    # street = 13
    print("Divide: ", street / 2)
    print("Modulus: ", street % 2 == 0)
    if (street % 2) == 0:
        print("Eastbound")
    else:
        print("Westbound")
    


calculate_street(11)

# even = (street % 2) == 0
# if street is even:
#     print("Eastbound")
# else:
#     print("Westbound")