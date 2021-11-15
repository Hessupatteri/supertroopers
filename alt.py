def sphere(): 
    print('Hello, this app will help you calculate the area of a sphere.')
    radius =float(input('Please submit the radius of the sphere: '))
    calculation=4*math.pi*(math.pow(radius, 2))
    print (f'The area of the sphere is {calculation:1.2f}, cm\u00b2.')
