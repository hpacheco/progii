import numpy as np
import matplotlib.pyplot as plt

dcc=plt.imread("../../../dados/dcc.jpg")
#print(dcc)
print(dcc.shape)
x,y,z = dcc.shape

plt.imshow(dcc)
#plt.show()
plt.savefig("dcc.jpg")