import base_functions as bf
import analysis as an
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process Image through CloudNine Algorithm')
    parser.add_argument("image_path", metavar="image_path", type=str, 
                        help="Path to HDF5 Image to process as per algorithm")
    args = parser.parse_args()
    filename = args.image_path
    data = bf.load_image(filename)
    bf.get_image_information(filename)

    bf.plot_hist_bin(data, 16)

    grey = an.get_grey_level_array(data)

    text = an.get_texture_analysis(data)

    shape = an.get_shape_analysis(data, False)
    #print(shape)

    finalArray = {
        "grey": grey,
        "texture": text,
        "shape": shape
    }

    print("Feature Array: ",finalArray)

def apply_algorithms(filename):
    data = bf.load_image(filename)      # load image
    grey = an.get_grey_level_array(data)    # grey-level array
    text = an.get_texture_analysis(data)    # texture analysis
    shape = an.get_shape_analysis(data, False)    # shape analysis
    finalArray = {
        "grey": grey,
        "texture": text,
        "shape": shape
    }

    return finalArray

if __name__ == "__main__":
    main()