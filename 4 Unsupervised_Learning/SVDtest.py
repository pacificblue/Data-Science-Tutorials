# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:31:31 2013

@author: hp
"""

from PIL import Image
from numpy import *

B=array([[-4,-1,2,3],[-2,-2,4,0],[-4,8,-4,0]])

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


A=B.T/sqrt(3)
U,S,rsV=linalg.svd(A)
print("rsV")
print(rsV)

y0 = dot(EV.T,B) # this is the compact trick
print("y0")
print(y0)

M = dot(B,B.T) # covariance matrix
e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
tmp = dot(B.T,EV).T # this is the compact trick
y1 = tmp[::-1] # reverse since last eigenvectors are the ones we want
S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
for i in range(y1.shape[1]):
  y1[:,i] /= S
print("y1")
print(y1)

U,S,y2 = linalg.svd(B)
print("y2")
print(y2)






