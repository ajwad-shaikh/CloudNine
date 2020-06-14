import numpy as np
import matplotlib.pyplot as plt
import h5py

def main():
    f = h5py.File('test2.h5', 'r')
    # print(*list(f['PRODUCT_INFORMATION'].attrs.items()), sep='\n')
    dset = f['VHRR']['Image Data']['VHRR_TIR']
    print(dset)
    data = np.array(dset[:,:])
    #show_image(data)
    plot_hist_bin(data, 16)

def load_image(filename): # give filename inside Dataset folder, returns numpy array
    f = h5py.File(filename, 'r')
    dset = f['VHRR']['Image Data']['VHRR_TIR']
    # print(dset)
    data = np.array(dset[:,:])
    return data

def show_image(data): # plot image using matplotlib, returns plot
    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.show()

def plot_hist(data): # plot histogram
    plt.hist(data.ravel())
    plt.show()

def plot_hist_bin(data, bins): # plot histogram with bins
    plt.hist(data.ravel(), bins=bins, histtype="bar")
    plt.show()

def get_image_information(filename):
    f = h5py.File(filename, 'r')
    print(*list(f['PRODUCT_INFORMATION'].attrs.items()), sep='\n')
    print(*list(f['PRODUCT_METADATA']['PRODUCT_DETAILS'].attrs.items()), sep='\n')

def show_images(images: list) -> None:
    n: int = len(images)
    f = plt.figure()
    for i in range(n):
        # Debug, plot figure
        f.add_subplot(1, n, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.axis('off')
    plt.show(block=True)

if __name__ == "__main__":
    main()