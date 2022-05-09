import numpy as np
import matplotlib.pyplot as plt

dcc=plt.imread("../../dados/dcc.jpg")
#print(dcc)
print(dcc.shape)
x,y,z = dcc.shape

dcc_big = np.empty((x*2, y*2, z), dtype=dcc.dtype)
for i,row in enumerate(dcc):
    for j,pixel in enumerate(row):
        dcc_big[i*2-1:i*2+1,j*2-1:j*2+1] = pixel

print(dcc_big.shape)
plt.imshow(dcc_big)
plt.show()