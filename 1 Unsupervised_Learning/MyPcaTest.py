# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:59:19 2013

@author: hp
"""

from PIL import Image
from numpy import *
from pylab import *

import mypca
import imtools
import os

imlist= imtools.get_imlist(os.curdir+"/pca_test")

im = array(Image.open(imlist[0])) # open one image to get size
m,n = im.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten()
              for im in imlist],'f')

# perform PCA
V,immean = mypca.mypca(immatrix)

# show some images (mean and 7 first modes)
fig=figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
  subplot(2,4,i+2)
  imshow(V[i].reshape(m,n))

fig.canvas.set_window_title("mypcaTest") 
show()