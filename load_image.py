import numpy as np
import matplotlib.pyplot as plt
import h5py

f = h5py.File('Dataset/test1.h5', 'r')
dset = f['VHRR']['Image Data']['VHRR_TIR']
print(dset)
data = np.array(dset[:,:])
plt.imshow(data, cmap='gray')
plt.show()