from __future__ import division

def divide(a,b):
    try:
        x = a/b
    except ZeroDivisionError
        x = np.inf
    return x

def multiply(a,b):
    return a*b    