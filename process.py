import base_functions as bf
import analysis as an

filename = "test2.h5"

# load image
data = bf.load_image(filename)
bf.get_image_information(filename)

# bf.plot_hist_bin(data, 16)

# grey-level array
gla = an.get_grey_level_array(data)

# texture analysis
feat = an.get_texture_analysis(data)

