#Uppgiften är att skriva ett program som räknar ut volymen fören liksidig kub samt en liksidig tetrahedron

import math
input("The mission is to calculate the volume of a cub and a tetrahedon. Start by pressing enter!"+"\n") # Telling the user what is coming.

cube_side=int(input("Enter tha length of the cubside, in centimeter, and than press enter again:")) # Asking the user to enter the length of the side of the cub.

cube_volume=cube_side**3 #Adding the varable and writing the folmula of the cub.
print("The calculated volume of the cube is: "+ str(cube_volume)+"cm3."+" "+"\n")#Printing the result

tetra_side=int(input("Now enter tha length of the tetrehedon, in centimeter, and than press enter again:"))# Asking the user to enter the length of the side of the tetrahedron.

tetra_volume=(tetra_side**3)/(6*math.sqrt(2)) #Adding the varable and writing the folmula of the volume of the tetrahedron V=a3/62
print("The volume of the cube is: "+ str(tetra_volume)+" cm3."+" "+"\n"+"\n")#Printing the result
print("You finished the mission."+" "+ "Good job!!")#Giving feedback
