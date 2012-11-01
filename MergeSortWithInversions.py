'''
Created on Oct 31, 2012

@author: naomiaro
'''

def merge(left, right):
    
    k = len(left) + len(right)
    
    left.append(float('inf'))
    right.append(float('inf'))
    
    l, r, inv = 0, 0, 0
    output = []
    for i in xrange(0, k):
        if left[l] <= right[r]:
            output.append(left[l])
            l = l + 1
        else:
            output.append(right[r])
            r = r + 1
            inv = inv + len(left) - l - 1 # (-1 because of added infinity)
            
    return output, inv

def mergesort(array):
    
    n = len(array)
    
    if n is 1:
        return array, 0
    
    m = n/2
    left = array[0:m]
    right = array[m:]
    
    left_sorted, l_inv = mergesort(left)
    right_sorted, r_inv = mergesort(right)
    
    output, inv = merge(left_sorted, right_sorted)
    #return total inversions in the array
    t_inv = l_inv + r_inv + inv
    
    return output, t_inv

if __name__ == '__main__':
    
    tests = [
        [1],
        [1, 2],
        [3, 2, 1],
        [6, 5, 4, 3, 2, 1],
        [5, 7, 2, 9, 0, 1, 2, 3, 8, 2, 9, 8, 0, 9, 9, 5, 6, 3, 6, 5, 6, 6, 6, 8]   
    ]
    
    try:
        for test in tests:
            print mergesort(test)
    except Exception, e:
        print e
    
    