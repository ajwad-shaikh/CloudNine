import base_functions as bf
import analysis as an

filename = "test2.h5"

# load image
data = bf.load_image(filename)
bf.get_image_information(filename)

bf.plot_hist_bin(data, 16)

# grey-level array
grey = an.get_grey_level_array(data)
#print(grey)

# texture analysis
text = an.get_texture_analysis(data)
#print(text)

# shape analysis
shape = an.get_shape_analysis(data, False)
#print(shape)

finalArray = {
    "grey": grey,
    "texture": text,
    "shape": shape
}

print(finalArray)