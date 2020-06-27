import os, glob
import base_functions as bf

VALIDATION_SET_PATH = "dataset/validation_set"
BACK_TO_ROOT_REF = "../.."

def main():
    printOptions()
    while True:
        print("Enter Choice: ")
        choice = input()
        if choice == '1':
            printOptions()
        elif choice == '2':
            showOptions()
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

if __name__ == "__main__":
    main()