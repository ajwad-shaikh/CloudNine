import numpy as np
import matplotlib.pyplot as plt
import h5py

if __name__ == "__main__":
    f = h5py.File('Dataset/test1.h5', 'r')
    dset = f['VHRR']['Image Data']['VHRR_TIR']
    print(dset)
    data = np.array(dset[:,:])
    plt.imshow(data, cmap='gray')
    plt.show()

def load_image(filename):
    f = h5py.File('Dataset/' + filename, 'r')
    dset = f['VHRR']['Image Data']['VHRR_TIR']
    print(dset)
    data = np.array(dset[:,:])
    return data

def show_image(data):
    plt.imshow(data, cmap='gray')
    plt.show()