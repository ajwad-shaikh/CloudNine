import base_functions as bf
import analysis as an
import os, random, glob

import process

from firebase import firebase

DATABASE_URL = "https://odk-x-push.firebaseio.com/"
TRAIN_SET_PATH = "dataset/train_set"

def main():
    os.chdir(TRAIN_SET_PATH)
    train_images = glob.glob("*.h5")
    dbReference = firebase.FirebaseApplication(DATABASE_URL, None)
    for image_path in train_images:
        finalArray = process.apply_algorithms(image_path)
        print(finalArray)
        print(dbReference.post('/cloudNine', finalArray))

if __name__ == "__main__":
    main()