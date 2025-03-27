import numpy as np
from numpy import asarray
from PIL import Image # package Pillow

dcc=asarray(Image.open("dcc.jpg"))
x,y,z = dcc.shape
print(dcc.shape)
dcc_t = np.transpose(dcc,axes=(2,0,1))
print(dcc_t.shape)

U, s, Vt = np.linalg.svd(dcc_t)
print(U.shape,s.shape,Vt.shape)

Sigma = np.zeros((z,x,y))
for pix in range(3):
    np.fill_diagonal(Sigma[pix, :, :], s[pix, :])

dcc_reconstructed_t = U @ Sigma @ Vt
print(dcc_reconstructed_t.shape)
dcc_reconstructed = np.transpose(dcc_reconstructed_t,axes=(1,2,0))
dcc_reconstructed = np.minimum(np.maximum(0,dcc_reconstructed),255)
print(dcc_reconstructed.shape)
Image.fromarray(dcc_reconstructed.astype("uint8")).save('dcc_svd.jpg')

r=100
dcc_compressed_t = U[:,:,:r] @ Sigma[:,:r,:r] @ Vt[:,:r,:]
dcc_compressed = np.transpose(dcc_compressed_t,axes=(1,2,0))
dcc_compressed = np.minimum(np.maximum(0,dcc_compressed),255)
Image.fromarray(dcc_compressed.astype("uint8")).save('dcc_compressed.jpg')

