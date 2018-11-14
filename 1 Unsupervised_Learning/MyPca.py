# -*- coding: utf-8 -*-
"""
Created on Sat Feb 09 23:55:21 2013

@author: hp
"""

from PIL import Image
from numpy import *

def mypca(X):
  """  Principal Component Analysis
    input: X, matrix with training data stored as flattened arrays in rows
    return: projection matrix (with important dimensions first), variance
    and mean."""

  # get dimensions
  num_data,dim = X.shape

  # center data
  mean_X = X.mean(axis=0)
  B = X - mean_X

  
  S = dot(B,B.T)/3# covariance matrix
  print("S")
  print(S)
  e,EV = linalg.eigh(S) # eigenvalues and eigenvectors
  e=e[::-1]
  print("e")
  print(e)
  EV=fliplr(EV)
  print("EV")
  print(EV)
  y0 = dot(EV.T,B) # this is the compact trick
  
  S = sqrt(e)
  print("S")
  print(S)
  

  # return the projection matrix, the variance and the mean
  return y0,mean_X
