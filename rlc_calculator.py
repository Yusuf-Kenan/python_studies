from math import pi

print("\n\n\n")
print("With this app you can calculate impedance of RLC current.".center(140))
print("\n")
print("You have to enter numeric values such as 5, 10, 100 and if you don't the app will keep asking...".center(140))

while True:
    print("\n\n")
    #ask user for resistor and ask again if the entry is not valid
    resistor = 0
    while True:
        try:
            resistor=float(input("Please enter resistor amount: "))
        except Exception as e :
            print("entry is not valid --->", e)
        else:
            break

    #ask user for coil and ask again if the entry is not valid
    coil = 0
    while True:
        try:
            coil=float(input("Please enter coil amount: "))
        except Exception as e :
            print("entry is not valid --->", e)
        else:
            break

    #ask user for condensor and ask again if the entry is not valid
    condenser = 0
    while True:
        try:
            condenser=float(input("Please enter condenser amount: "))
        except Exception as e :
            print("entry is not valid --->", e)
        else:
            break

    #ask user for frequency and ask again if the entry is not valid
    frequency = 0
    while True:
        try:
            frequency=float(input("Please enter frequency amount: "))
        except Exception as e :
            print("entry is not valid --->", e)
        else:
            break

    #Calculate the impedance of RLC current with the given values by user
    #xl=2pifL
    xl = 2 * pi * frequency * coil
    #xc=1/2pifc
    xc = 1 / (2 * pi * frequency * condenser)
    #z= ((xl-xc)**2 + R**2) ** (1/2)
    x = xl-xc
    z = (x ** 2 + resistor ** 2) ** 0.5

    print("\n")
    print(f"The result is: {z:10.3f}".center(150))

    yes_or_no=input("Would you like to try again: y/n  ")
    if yes_or_no == "n":
        break
