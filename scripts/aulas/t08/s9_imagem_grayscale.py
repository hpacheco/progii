import numpy as np
import matplotlib.pyplot as plt

dcc=plt.imread("../t06/dcc.jpg")

dcc_gray = dcc.mean(axis=2)

print(dcc_gray)
plt.imshow(dcc_gray,cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.savefig('gray.png')