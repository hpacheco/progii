import numpy as np
from numpy import asarray
from PIL import Image

dcc=asarray(Image.open("../../../dados/dcc.jpg"))
print(dcc.shape)
x,y,z = dcc.shape

dcc_big = np.empty((x*2, y*2, z), dtype=dcc.dtype)
for i,row in enumerate(dcc):
     for j,pixel in enumerate(row):
         dcc_big[i*2-1:i*2+1,j*2-1:j*2+1] = pixel
Image.fromarray(dcc_big).save('dcc2x.jpg')
