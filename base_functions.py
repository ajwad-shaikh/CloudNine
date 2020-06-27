import numpy as np
import matplotlib.pyplot as plt
import h5py
import math

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

def show_images(images: list):
    n = len(images)
    root_n = math.ceil(math.sqrt(n))
    f, ax = plt.subplots(nrows=root_n, ncols=root_n)
    for i in range(n):
        # Debug, plot figure
        ax[i//root_n, i%root_n].imshow(images[i], cmap='gray')
        ax[i//root_n, i%root_n].set_title("Image Id: {}".format(i))
        ax[i//root_n, i%root_n].axis('off')
        # f.add_subplot(root_n, root_n, i+1)
        # plt.imshow(images[i], cmap='gray')
        # plt.axis('off')
    plt.show(block=True)

def show_result(sourceImageData, matchImageData, heading):
    fig, (ax1,ax2) = plt.subplots(1, 2)
    plt.suptitle(heading)
    ax1.imshow(sourceImageData['image'], cmap='gray')
    ax1.set_title("Source Image: {}".format(sourceImageData['name']))
    ax1.axis('off')
    ax2.imshow(matchImageData['image'], cmap='gray')
    ax2.set_title("Match Image: {}".format(matchImageData['name']))
    ax2.axis('off')
    plt.show(block=True)

if __name__ == "__main__":
    main()