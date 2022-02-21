import numpy as np
import matplotlib.pyplot as plt

dcc=plt.imread("../dados/dcc.jpg")
print(dcc.shape)
x,y,z = dcc.shape

dcc_blur = np.empty((x,y,z),dtype=dcc.dtype)

# blurriness level
blur = 5

for i in range(x):
    for j in range(y):
        pixes = dcc[max(0,i-blur):i+blur+1,max(0,j-blur):j+blur+1]
        dcc_blur[i,j] = pixes.mean(axis=(0,1))

plt.imshow(dcc_blur)
plt.axis('off')
plt.savefig('test.png')