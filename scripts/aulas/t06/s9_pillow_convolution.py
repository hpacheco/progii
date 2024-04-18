import numpy as np
from numpy import asarray
from PIL import Image # package Pillow
import math

def convolution2d(image, w):
    m, _ = w.shape # kernel must be an odd square matrix
    a = math.floor(m/2)
    x = image.shape[0]
    y = image.shape[1]
    new_image = np.zeros((x,y,z),dtype="uint8")
    for i in range(x):
        for j in range(y):
                im = image[max(0,i-a):i+a+1,max(0,j-a):j+a+1]
                kern = w[max(0,a-i):min(m,m+x-i-a-1),max(0,a-j):min(m,m+y-j-a-1)]
                kern = kern.reshape(kern.shape+(1,))
                s = np.sum(im*kern,axis=(0,1))
                s = np.minimum(np.maximum(0,s),255)
                new_image[i][j] = s
    return new_image

dcc=asarray(Image.open("../../../dados/dcc.jpg"))
x,y,z = dcc.shape

w_gaussian = 1/256 * np.array([[1,4,6,4,1],[4,16,24,26,4],[6,24,36,24,6],[4,16,24,26,4],[1,4,6,4,1]])
dcc_blur = convolution2d(dcc,w_gaussian)
Image.fromarray(dcc_blur).save('dcc_blur.jpg')

w_sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
dcc_blur = convolution2d(dcc,w_sharpen)
Image.fromarray(dcc_blur).save('dcc_sharpen.jpg')

w_emboss = np.array([[-2,-1, 0],[-1,1,1],[0,1,2] ])
dcc_blur = convolution2d(dcc,w_emboss)
Image.fromarray(dcc_blur).save('dcc_emboss.jpg')

