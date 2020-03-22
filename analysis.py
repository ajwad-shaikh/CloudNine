import numpy as np
from skimage.feature import greycoprops, greycomatrix, shape_index, canny
from skimage.morphology import opening, closing, disk
from skimage.measure import perimeter
import base_functions as bf

def main():
    data = bf.load_image("test2.h5")
    thres = np.quantile(data.ravel(), 0.65)
    bindata = data // thres
    op_selem = disk(6)
    close_selem = disk(12)
    opened = opening(bindata, op_selem)
    closed = closing(opened, close_selem)
    peri = perimeter(closed)
    area = np.count_nonzero(closed == 1)
    compact = 4 * np.pi * area / (peri**2)
    print(peri, area, compact)
    bf.show_images([data, bindata, opened, closed, canny(closed)])

def get_grey_level_array(data): # returns 16-bin grey-level distribution
    return np.histogram(data.ravel(), bins=16)[0]

def get_texture_analysis(data): # returns grey-level cooccurennce matrix properties in array form
    glcm = greycomatrix(data, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], 1024, normed=False)
    con = greycoprops(glcm, 'contrast')
    enr = greycoprops(glcm, 'energy')
    cor = greycoprops(glcm, 'correlation')
    dis = greycoprops(glcm, 'dissimilarity')
    feat_array = [con[0], enr[0], cor[0], dis[0]]
    means = np.mean(feat_array, axis=1)
    std_dev = np.std(feat_array, axis=1)
    return np.concatenate((means, std_dev))

def get_shape_analysis(data, show_plot): # returns shape analysis features and plots
    thres = np.quantile(data.ravel(), 0.65)
    bindata = data // thres
    op_selem = disk(6)
    close_selem = disk(12)
    opened = opening(bindata, op_selem)
    closed = closing(opened, close_selem)
    peri = perimeter(closed)
    area = np.count_nonzero(closed == 1)
    compact = (peri**2) / (4 * np.pi * area)
    if show_plot:
        bf.show_images([data, bindata, opened, closed, canny(closed)])
    return([peri, area, compact])
    

if __name__ == "__main__":
    main()