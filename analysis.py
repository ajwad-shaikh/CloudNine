import numpy as np
import skimage.feature as sk

if __name__ == "__main__":
    data = np.array([ [1,1,1,1] , [2,2,2,2]])
    print(np.histogram(data.ravel(), bins=16)[0])

def get_grey_level_array(data): # returns 16-bin grey-level distribution
    return np.histogram(data.ravel(), bins=16)[0]

def get_texture_analysis(data): # returns grey-level cooccurennce matrix properties in array form
    glcm = sk.greycomatrix(data, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], 1024, normed=False)
    con = sk.greycoprops(glcm, 'contrast')
    enr = sk.greycoprops(glcm, 'energy')
    cor = sk.greycoprops(glcm, 'correlation')
    dis = sk.greycoprops(glcm, 'dissimilarity')
    feat_array = [con[0], enr[0], cor[0], dis[0]]
    means = np.mean(feat_array, axis=1)
    std_dev = np.std(feat_array, axis=1)
    return np.concatenate((means, std_dev))
    