import base_functions as bf
import analysis as an
import os, random, glob

from firebase import firebase

train_path = "Dataset/train_set"
os.chdir(train_path)

filelist = glob.glob("*.h5")

firebase = firebase.FirebaseApplication("https://odk-x-push.firebaseio.com/", None)

for file in filelist:
    data = bf.load_image(file)
    # bf.get_image_information(filename)

    # grey-level array
    grey = an.get_grey_level_array(data)

    # texture analysis
    text = an.get_texture_analysis(data)

    # shape analysis
    shape = an.get_shape_analysis(data, False)

    finalArray = { 
        "filename": file,
        "grey": grey,
        "texture": text,
        "shape": shape
    }

    print(finalArray)

    print(firebase.post('/cloudNine', finalArray))