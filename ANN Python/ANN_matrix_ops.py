# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 10:30:27 2015

@author: Alex

Neural Network 1: Matrix Operations
"""
from matrix import Matrix
from matrixMath import MatrixMath
    

def main():
    row = 3
    col = 3
    
    math = MatrixMath()
    m1 = Matrix(row, col)        
    m2 = Matrix(row, col)
    m1.randomize(1.0, 10.0)
    m2.randomize(1, 10)
    
    addition = math.add(m1.matrix, m2.matrix)
    div = math.divide(m1.matrix, m2.matrix)    
    dot = math.dotProduct(m1.matrix, m2.matrix)
    
    print "Matrix 1: \n", m1.matrix
    print "Matrix 2: \n", m2.matrix    
    print "Added result: \n", addition    
    print "Divided by scalar: \n", div
    
    print "Dot product: \n", dot
    
if __name__ == "__main__":
    main()    
