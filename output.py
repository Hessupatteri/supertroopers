# alt.py
def sphere(): 
    print('Hello, this app will help you calculate the area of a sphere.')
    radius =float(input('Please submit the radius of the sphere: '))
    calculation=4*math.pi*(math.pow(radius, 2))
    print (f'The area of the sphere is {calculation:1.2f}, cm\u00b2.')


# aras.py
def tetrahedron(): 
    print('This app will help you calculate the volume of a tetrahedron!\n')
    base =float(input('Enter the length(cm) of the base of your tetrahedron: '))
    hight =float(input('Please also enter the length(cm) of the hight: '))
    calculation=((base*hight)/3)
    print("")
    print (f'The volume of the tetrahedron is {calculation} cm\u00b2.')


# jani.py
def cube():
    while True:
        try:
            cubeside = eval(input("Insert cube side length in meters:"))
            cubevolume = cubeside ** 3
            print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nThe volume of the cube is {cubevolume}m^3\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            break
        except NameError:
            print("Please insert number values, for example 10, 25.5 , 100 etc.")

# jogu.py
def triangle():
    try:
        trianglebase = float(input("What is the length of the base of the triangle?")) #put in the length of triangle
        triangleheight = float(input("What is the height of the triangle?")) #put in the height of triangle
    except ValueError:
            while True:
                try:
                    trianglebase = float(input("Must be a valid number"))
                except ValueError:
                    pass
                else:
                    break
    areatriangle = trianglebase*triangleheight/2 #calculates the area of the triangle
    print("\nThe area triangle is",round(areatriangle,2),"cm^2") #prints the area of the triangle

# joli.py
def octagon_area():
    side = eval(input(f'\nInsert octagon side length in centimeters '))
    area = 2*side*2*(1+math.sqrt(2))

    return f'\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nThe area of your octagon is {int(area)} cm^2\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'



# sax.py
def cone():

    radie_cone = eval(input("\nPlease enter the radie of the cone!\n"))
    height_cone = eval(input("\nPlease enter the height of the cone!\n"))
    print(f"\nIf the radie of the cone is {radie_cone} and the height is {height_cone} cm then the volume is {1/3*3.14*radie_cone**2*height_cone} cm^3.")


import math

#Här under hittar ni era namn där ni ska ange funktionen ni vill anropa som ni får definiera här ovanför.
#ändra choice text strängen med er valda objekt.

while True:
    try:
        choice = eval(input("1:Cube\n2:Sphere\n3:Octagon\n4:triangle\n5:cone\n6:tetrahedron\nVolume calculator, input choice:"))
        if choice == 1:
            cube()
        elif choice == 2:
            sphere()
        elif choice == 3:
            print(octagon_area())
        elif choice == 4:
            triangle()
        elif choice == 5:
            cone()        
        elif choice == 6:
            tetrahedron()
    except NameError:
        print("Error! Error! Error! Invalid input, try again.")
