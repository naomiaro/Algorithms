'''
Created on Nov 3, 2012

@author: naomiaro
'''

import math

def euclideanDistance(p, q):
    
    total = 0
    for i in xrange(0, len(p)):
        total = total + math.pow(p[i] - q[i], 2)
        
    return math.sqrt(total)

"""
Base case for recursion
"""
def findClosestPair(P):
    
    best = float('inf')
    pair = None
    for i in xrange(0, len(P) - 1):
        for j in xrange(1, len(P) - i):
            p = P[i]
            q = P[i+j]
            d = euclideanDistance(p, q)
            
            if d < best:
                best = d
                pair = (p, q)
                
    return pair
    
def closestSplitPair(Px, Py, delta):
    mid_x = Px[len(Px)/2][0]
    low = mid_x - delta
    high = mid_x + delta
    Sy = [p for p in Py if p[0] >= low and p[0] <= high]
    
    best = delta
    pair = None
    len_Sy = len(Sy)
    
    if len_Sy < 8:
        pair = findClosestPair(Sy)
        d = euclideanDistance(pair[0], pair[1])
        
        if d >= best:
            pair = None
    else:
       
        for i in xrange(0, len_Sy - 7):
            for j in xrange(1, 8):
                p = Sy[i]
                q = Sy[i+j]
                d = euclideanDistance(p, q)
                
                if  d < best:
                    best = d
                    pair = (p,q)

    return pair
    

def closestPair(Px, Py):
    mid = len(Px)/2
    
    Qx = Px[0:mid]
    Rx = Px[mid:]
    Qy = Py[0:mid]
    Ry = Py[mid:]
    points = {}
    
    if len(Px) < 8:
        return findClosestPair(Px)
    
    pair1 = closestPair(Qx, Qy)
    pair2 = closestPair(Rx, Ry)
    
    if pair1 is not None:
        d1 = euclideanDistance(pair1[0], pair1[1])
    else:
        d1 = float('inf')
    
    if pair2 is not None:
        d2 = euclideanDistance(pair2[0], pair2[1])
    else:
        d2 = float('inf')
    
    delta = min(d1, d2)
    
    pair3 = closestSplitPair(Px, Py, delta)
    
    if pair3 is not None:
        d3 = euclideanDistance(pair3[0], pair3[1])
    else:
        d3 = float('inf')
   
    try:
        points[d1] = pair1
        points[d2] = pair2
        points[d3] = pair3
    except:
        pass
    
    keys = points.keys()
    keys.sort()
    
    return points[keys[0]]
    
    

if __name__ == '__main__':
    #P = [(1,1), (3,3), (4,6), (3,5), (4, 3.5), (8,9), (11,6), (20,3), (15, 15)]
    
    P = [(1,1), (3,3), (11,5), (45,47), (4,6), (3,5), (4, 3.5), (65, 3), (33, 22), (3, 7), (3, 11), (4, 14), (4, 4), (4, 16)]
    Px = sorted(P, key=lambda tup: tup[0])
    Py = sorted(P, key=lambda tup: tup[1])

    pair = closestPair(Px, Py)
    
    print pair
    