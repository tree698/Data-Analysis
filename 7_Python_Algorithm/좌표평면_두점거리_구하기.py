"""
a = (1,2)
b = (3,4)

(0,0) 0행 0열
(1,2) 1행 2열
"""
a = (1,2)
b = (3,4)
print(type(a))

result = ((3-1)**2) + ((4-2)**2)
print(round(result**(1/2),2))

def distance(a, b):
    x_distance = abs(a[0]-b[0])**2
    y_distance = abs(a[1]-b[1])**2
    return round((x_distance + y_distance)**(1/2), 2)

print(distance(a, b))
