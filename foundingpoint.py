import math
def balanceFinder(k1,k2):
    
    a = k1[0]-k2[0]
    b = k1[1]-k2[1]
    c = k1[2]-k2[2]
    d=b*b-4*a*c
    x = [0,0]
    if (d>=0):
        x[0] = (-b + math.sqrt(d))/(2*a)
        x[1] = (-b - math.sqrt(d))/(2*a)
    else:
        print('Korni ne dejstvitel\'ni')
    
    return x
