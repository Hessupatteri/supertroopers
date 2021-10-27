import math

def cube():
    while True:
        try:
            cubeside = eval(input("Insert cube side length in meters:"))
            cubevolume = cubeside ** 3
            print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nThe volume of the cube is {cubevolume}m^3\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            break
        except NameError:
            print("Please insert number values, for example 10, 25.5 , 100 etc.")

def octagon_area():
    side = eval(input(f'\nInsert octagon side length in centimeters '))
    area = 2*side*2*(1+math.sqrt(2))

    return f'\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nThe area of your octagon is {int(area)} cm^2\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

#Här under hittar ni era namn där ni ska ange funktionen ni vill anropa som ni får definiera här ovanför.
#ändra choice text strängen med er valda objekt.

while True:
    try:
        choice = eval(input("1:Cube\n2:Alva\n3:Octagon\n4:Joel\n5:Markus\n6:Sara\nVolume calculator, input choice:"))
        if choice == 1:
            cube()
        elif choice == 2:
            # Alva()
            print('Alva')
        elif choice == 3:
            print(octagon_area())
        elif choice == 4:
            # Joel()
            print('Joel')
        elif choice == 5:
            # Markus()
            print('Markus')
        elif choice == 5:
            # Sara()
            print('Sara')
    except NameError:
        print("Error! Error! Error! Invalid input, try again.")