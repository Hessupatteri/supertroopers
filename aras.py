def tetrahedron(): 
    print('This app will help you calculate the volume of a tetrahedron!\n')
    base =float(input('Enter the length(cm) of the base of your tetrahedron: '))
    hight =float(input('Please also enter the length(cm) of the hight: '))
    calculation=((base*hight)/3)
    print("")
    print (f'The volume of the tetrahedron is {calculation} cm\u00b2.')
