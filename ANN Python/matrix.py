# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 17:17:23 2015

@author: Alex

    Primary matrix class for ANN operations

"""
from copy import deepcopy
import numpy as np
from random import Random

class Matrix: 
    # Initializes to zero matrix
    def __init__(self, row, col):
        self.row = row
        self.col = col        
        self.matrix =  [[0 for x in range(self.row)] for x in range(self.col) ]
   
   # String representation of matrix    
    def __str__(self):
        return str(self.__dict__)
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # Allows index access to matrix, ex: matrix[2][3]
    def this(self, row, col):
        return self.matrix[row][col]
    
    # Get the number of rows in the matrix
    def getNumRow(self):
        return self.row
        
    # Get the number of columns in the matrix    
    def getNumCol(self):
        return self.col
    
    # Converts 2d list to 1d array of floats           
    def toPackedArray(self):
        pass
    
    # TO be added
    def fromPackedArray(self):
        pass
    
    # Create random matrix with single column
    def createColumnMatrix(self, values):
        self.matrix = self.matrix.append([values])
            
    # Create random matrix with single row.
    def createRowMatrix(self, row):
        for i in row:
            self.matrix.append(np.random.rand)
    
    # Adds the value to every cell in the matrix    
    def add(self, row, col, value):
        pass
    
    # Set every cell in a matrix to zero
    def clear(self):
        self.matrix = [[0 for x in range(self.row)] for x in range(self.col) ]

    # Clones matrix object
    def clone(self):
        return self.matrix
    
    # Determines if matrices are equal with precision
    def equals(self, precision):
        pass

    # Gets one column from matrix obj as new matrix obj
    def getCol(self, col):
        pass
    
    # Gets one row from matrix obj as new matrix obj
    def getRow(self, row):
        pass
        
    # isZero: Determines if every cell in a matrix object is zero.    
    def isZero(self):
        pass

    def randomize(self, minimum, maximum):
        self.matrix = np.random.randint(minimum,maximum, size=(self.row, self.col))
        
    # sumCell: Returns the sum of every cell in a matrix obj
    def sumCell(self):
        pass
    
    # Sets the value of a cell
    def setCell(self, row, col, value):
        self.matrix[row][col] = value




    