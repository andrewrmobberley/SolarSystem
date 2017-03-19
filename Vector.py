import numpy as np
import math as m

def SqMag(c):
    """ 
    Finds the square magnitude.
    :param c: element of array
    :return: The sum of squares of each element => square magnitude
    """
    return c[0]**2 + c[1]**2 + c[2]**2

def Mag(c):
    """ 
    Finds the magnitude.
    :param c: array
    :return: The square root of the sum of squares of each element => magnitude
    """
    return m.sqrt(c[0]**2 + c[1]**2 + c[2]**2)


def add(v1, v2 ):                       
    """ 
    Finds the sum of two vectors.
    :param v1: The first vector
    :param v2: The second vector
    :return: The sum of the corresponding vector elements arranged as new 1x3 vector
    """
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    z = v1[2] + v2[2]
    return np.array([ x, y, z ])

def multsca(a,v1):
    """ 
    Finds the resulting vector when multiplied by a scalar.
    :param a: scalar quantity
    :param v1: vector v1
    :return: The product of each vector element with scalar a arranged as new 1x3 vector
    """
    x = a*v1[0]
    y = a*v1[1]
    z = a*v1[2]
    return np.array([ x,y,z ])

def divsca(a,v1):
    """ 
    Divides the vector elements by a scalar number
    :param v1: element of vector 1 
    :param a: scalar number
    :return: the divided elements of vector 1 in a 1x3 array 
    """
    x = v1[0]/a
    y = v1[1]/a
    z = v1[2]/a
    return np.array([ x,y,z ])

def sub(v1, v2 ):
    """ 
    Finds the difference between two vectors by subtracting the appropriate elements. 
    :param v1: element of vector 1 
    :param v2: element of vector 2
    :return: vector 1 - vector 2
    """
    x = v1[0] - v2[0]
    y = v1[1] - v2[1]
    z = v1[2] - v2[2]
    return np.array([ x, y, z ])

def dot(v1,v2):
    """ 
    Finds the dot product of two vectors. 
    :param v1: element of vector 1 
    :param v2: element of vector 2
    :return: the dot product
    """
    x = v1[0] * v2[0]
    y = v1[1] * v2[1]
    z = v1[2] * v2[2]
    return x + y + z

def cross(v1,v2):
    """ 
    Finds the cross product of two vectors . 
    :param v1: element of vector 1
    :param v2: element of vector 2
    :return: vector cross product in a 1x3 array 
    """
    x = v1[1]*v2[2] - v1[2]*v2[1]
    y = v1[2]*v2[0] - v1[0]*v2[2]
    z = v1[0]*v2[1] - v1[1]*v2[0]
    return np.array([ x,y,z ])
