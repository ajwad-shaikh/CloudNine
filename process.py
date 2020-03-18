import base_functions as bf
import numpy as np
import skimage.feature as sk

# load image
data = bf.load_image("test2.h5")
bf.plot_hist_bin(data, 16)

# grey-level array
gla = bf.get_grey_level_array(data)

# texture analysis
glcm = sk.greycomatrix(data, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], 1024)
con = sk.greycoprops(glcm, 'contrast')
enr = sk.greycoprops(glcm, 'energy')
cor = sk.greycoprops(glcm, 'correlation')
dis = sk.greycoprops(glcm, 'dissimilarity')
print(con, enr, cor, dis)