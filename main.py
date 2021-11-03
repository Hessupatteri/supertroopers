import math

#Här under hittar ni era namn där ni ska ange funktionen ni vill anropa som ni får definiera här ovanför.
#ändra choice text strängen med er valda objekt.

while True:
    try:
        choice = eval(input("1:Cube\n2:Sphere\n3:Octagon\n4:Joel\n5:Markus\n6:Sara\nVolume calculator, input choice:"))
        if choice == 1:
            cube()
        elif choice == 2:
            sphere()
        elif choice == 3:
            print(octagon_area())
        elif choice == 4:
            # Joel()
            print('Joel')
        elif choice == 5:
            cone()        
            elif choice == 5:
            # Sara()
            print('Sara')
    except NameError:
        print("Error! Error! Error! Invalid input, try again.")
