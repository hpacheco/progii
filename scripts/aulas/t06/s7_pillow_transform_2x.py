import numpy as np
from numpy import asarray
from PIL import Image # package Pillow

dcc=asarray(Image.open("dcc.jpg"))
x,y,z = dcc.shape
print(x,y,z)

V = np.zeros((x*2,x),dtype="uint8")
np.fill_diagonal(V[0::2,:],np.ones((x)))
np.fill_diagonal(V[1::2,:],np.ones((x)))

H = np.zeros((y,y*2),dtype="uint8")
np.fill_diagonal(H[:,0::2],np.ones((y)))
np.fill_diagonal(H[:,1::2],np.ones((y)))

dcc_big = np.zeros((x*2,y*2,z),dtype="uint8")
for pix in range(z):
    dcc_big[:,:,pix] = V @ dcc[:,:,pix] @ H
Image.fromarray(dcc_big).save('dcc_2x.jpg')

