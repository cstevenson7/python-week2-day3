from math import pi

def circumference(radius=0, diameter=0):
    if diameter != 0:
        circle_size  = pi * diameter
        return (f'The circumference of your circle is {round(circle_size,4)}')
    else:
        circle_size  = pi * radius *2    
        return (f'The circumference of your circle is {round(circle_size,4)}')

#print(circumference(0,6))

def area(l,w):
    area = l* w
    message = (f'\nThe square footage or area with a length of {l} and a width of {w} is {area}')
    return message
 
#print (area(5,3))
