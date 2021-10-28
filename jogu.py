import math
try:
    lengthtetra = float(input("What is the length of the tetrahedron?")) #put in the length of tetrahedron

except ValueError:
        while True:
            try:
                lengthtetra = float(input("Must be a valid number"))

            except ValueError:
                pass
            else:
                break
volumetetra = lengthtetra**3/6*math.sqrt(2) #multiples the tetrahedrons lenght by 3, divdes it by 6 and then take the sqaure root of 2
print("\nThe tetrahedrons volume is",round(volumetetra,2),"cm^3") #prints the tetrahedrons volume