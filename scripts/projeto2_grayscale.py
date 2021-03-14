import matplotlib.pyplot as plt
import numpy as np
dcc=plt.imread('../dados/dcc.jpg')

# flatten 3D array to 2D array
w,h,rgb = dcc.shape
# array of RGB colors
colors = dcc.reshape((w*h),rgb)

# luminosity of a color
def luminosity(rgb):
    return 0.21 * rgb[0] + 0.72 * rgb[1] + 0.07 * rgb[2]

# array of grayscale colors
grayscales = np.apply_along_axis(luminosity,1,colors)

# draw a grayscale histogram
plt.hist(grayscales,bins=256,color='grey')
plt.show()





