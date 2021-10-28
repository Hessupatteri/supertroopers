def sphere(radie_sphere):
     return 4/3*3.14*radie_sphere**3
#funtion that calculates the volume of the sphere. 

def cone(radie_cone, height_cone):
    return 1/3*3.14*radie_cone**2*height_cone
#Function that calculates the volume of the cone.   


form = input("\n\nWelcome! Tell me the form of the figure. \n\nPlease enter 1 if it´s a sphere or 2 if it´s a cone?\n")
#create variabel so i can use it in functions. Need to be input about the form. 

if form =="1":
    radie_sphere=float(input("\nPlease enter the radie of the sphere!\n"))
    print(f"\nIf the radie of your sphere is {radie_sphere} cm then the volume is", sphere(radie_sphere), "cm^3.")
elif form =="2":
    radie_cone=float(input("\nPlease enter the radie of the cone!\n"))
    height_cone=float(input("\nPlease enter the height of the cone!\n"))
    print(f"\nIf the radie of the cone is {radie_cone} and the height is {height_cone} cm then the volume is", cone(radie_cone, height_cone), "cm^3.")
else: 
    print("Sorry, can´t understand. Please try again.")
