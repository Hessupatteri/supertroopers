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