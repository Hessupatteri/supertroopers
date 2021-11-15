def octagon_area():
    side = eval(input(f'\nInsert octagon side length in centimeters '))
    area = 2*side*2*(1+math.sqrt(2))

    return f'\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nThe area of your octagon is {int(area)} cm^2\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

