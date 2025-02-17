import numpy as np
from numpy import asarray
from PIL import Image # package Pillow

dcc=asarray(Image.open("../../../dados/dcc.jpg"))
x,y,z = dcc.shape

dcc_rotate = np.transpose(dcc,axes=(1,0,2))
dcc_rotate = dcc_rotate[:,::-1,:]

Image.fromarray(dcc_rotate).save('dcc_rotate.jpg')

