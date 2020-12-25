import numpy as np

p1 = np.array([1,1])
p2 = np.array([4,4])

def distance(p1,p2):
    """Finds the distance between p1 and p2"""
    return np.sqrt(sum(np.power(p2-p1, 2)))


print(distance(p1,p2))
