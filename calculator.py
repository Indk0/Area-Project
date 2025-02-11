import math

print('Area Calculator')

print('Please select the following shapes for an area calculation.')
print('Please make sure to have the measurements.')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

shape = int(input('Chosen shape: '))

if shape == 1:
    print('You have picked a triangle.')
    height = int(input('What is the height of your triangle?: '))
    base = int(input('What is the length of the base of your triangle?: '))
    ac1 = (height * base)/2
    print('The area of your triangle is',ac1)
elif shape == 2:
    print('You have picked a rectangle.')
    length = int(input('What is the length of your rectangle?: '))
    width = int(input('What is the width of your rectangle?: '))
    ac2 = length*width
    print('The area of your rectangle is', ac2)
elif shape == 3:
    print('You have picked a square.')
    side = int(input('What is the length of your square?: '))
    ac3 = side**2
    print('The area of your square is', ac3)
elif shape == 4:
    print('You have picked a circle.')
    radius = int(input('What is the radius of your circle?: '))
    ac4 = math.pi * (radius ** 2)
else shape == 5:
    print('You session has come to an end.')