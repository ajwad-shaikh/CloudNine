import os, glob
import base_functions as bf
import urllib.request as request
import json

VALIDATION_SET_PATH = "dataset/validation_set"
BACK_TO_ROOT_REF = "../.."
TRAIN_DATA = { }

def main():
    printOptions()
    while True:
        print("Enter Choice: ")
        choice = input()
        if choice == '1':
            printOptions()
        elif choice == '2':
            showOptions()
        elif choice == '3':
            print(fetchTrainData())
        elif choice == '4':
            searchQuery()
        else:
            break


def printOptions():
    os.chdir(VALIDATION_SET_PATH)
    validation_images = glob.glob("*.h5")
    for image in validation_images:
        print(image)
    os.chdir(BACK_TO_ROOT_REF)

def showOptions():
    os.chdir(VALIDATION_SET_PATH)
    validation_images = glob.glob("*.h5")
    images = []
    for image in validation_images:
        image_data = bf.load_image(image)
        images.append(image_data)
    bf.show_images(images)
    os.chdir(BACK_TO_ROOT_REF)

def fetchTrainData():
    global TRAIN_DATA
    if not TRAIN_DATA:
        with request.urlopen('https://odk-x-push.firebaseio.com/cloudNine.json') as response:
            if response.getcode() == 200:
                source = response.read()
                TRAIN_DATA = json.loads(source)
            else:
                print('An error occurred while attempting to retrieve data from the API.')
    return TRAIN_DATA

def searchQuery():
    global TRAIN_DATA
    if not TRAIN_DATA:
        if not fetchTrainData():
            print("Could Not Search due to possible Network Error")
    query_image_id = int(input("Enter Search Image Id: "))
    os.chdir(VALIDATION_SET_PATH)
    validation_images = glob.glob("*.h5")
    query_image_data = bf.load_image(validation_images[query_image_id])
    os.chdir(BACK_TO_ROOT_REF)
    bf.show_image(query_image_data)
    
if __name__ == "__main__":
    main()