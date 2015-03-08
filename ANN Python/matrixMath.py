# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 18:05:33 2015

@author: Alex

    Primary matrix math class. Performs math based matrix operations

"""
import numpy as np

class MatrixMath():
    # add: Adds two matrixes and produces a third matrix
    def add(self, matrix_a, matrix_b):
        # Will hold new matrix        
        matrix = []
        try:        
            matrix = np.add(matrix_a, matrix_b)
            return matrix
        except np.ERR_RAISE, e:
            print ("An error occurred: ", e)
        
        
    # copy: Copies one matrix unto another
    def copy(matrix_a, matrix_b):
        matrix_b = matrix_a
        return matrix_a, matrix_b

    # delCol: Delete a column in a matrix    
    def delCol(matrix, deleted):
        return matrix

    # delRow: Delete a row in a matrix    
    def delRow(matrix, deleted):
        return matrix

    # divide: Divides one matrix by a scalr and produces a second matrix    
    def divide(self, matrix, scalar):
        try:
            matrix = np.divide(matrix, scalar)
            return matrix
        except np.ERR_RAISE, e:
            print ("An error occurred: ", e)
        
    # dotProduct: Calculates the dot product of a matrix
    def dotProduct(self, matrix_a, matrix_b):
        matrix = []
        try:
            matrix = np.add(matrix_a, matrix_b)        
            return matrix
        except np.ERR_RAISE, e:
            print ("An error occurred: ", e)
            
    # identity: creates an identity matrix of a specified size
    def identity(size):
        matrix = []
        return matrix
        
    # multiply: Multiplies two matrices    
    def multiply(matrix_a, matrix_b):
        matrix = []
        return matrix
    
    # multiplyScalar: Multiplies a matrix by a scalar         
    def multiplyScalar(matrix, a):
        return matrix
     
    # subtract: Subtracts two matrices 
    def subtract(matrix_a, matrix_b):
        matrix = []
        return matrix
     
    # transpose: Transposes a matrix and produces a new matrix
    def transpose(matrix_a, matrix_b):
        matrix = []
        return matrix
    # vectorLength: Calculates the squared length of a vector
        
    def vectorLength(matrix):
        return matrix
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        