import os, glob, sys, math, statistics as stat
import base_functions as bf
import urllib.request as request
import process
import json

VALIDATION_SET_PATH = "dataset/validation_set"
TRAIN_SET_PATH = "dataset/train_set"
BACK_TO_ROOT_REF = "../.."
TRAIN_DATA = {}
CHECK_DATA = -1

def main():
    global CHECK_DATA
    CHECK_DATA = getDatasetStatus()
    print("\n\n************** CloudNine **************\n")
    if CHECK_DATA == 1:
        print("Full Fledged Mode Active: All data present!")
    elif CHECK_DATA == 0:
        print("MVP Mode Active: Only Validation Data present!")
    elif CHECK_DATA == -1:
        print("No Dataset Available -> Read instructions from README")
        return
    while True:
        choice = input("\n1: Show Validation Images\n2: Fetch Train Data from Remote Database\n3: Begin Search Query\nEnter any other choice to exit\nEnter Choice: ")
        if choice == '1':
            showOptions()
        elif choice == '2':
            fetchTrainData()
        elif choice == '3':
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
    global TRAIN_DATA, CHECK_DATA
    if not TRAIN_DATA:
        if not fetchTrainData():
            print("Could Not Search due to possible Network Error")
    query_image_id = int(input("Enter Search Image Id: "))
    os.chdir(VALIDATION_SET_PATH)
    validation_images = glob.glob("*.h5")
    source_image_name = validation_images[query_image_id]
    source_image_data = bf.load_image(source_image_name)
    sourceFinalArray = process.apply_algorithms(source_image_name)
    os.chdir(BACK_TO_ROOT_REF)
    
    match_image_name = compare(sourceFinalArray)
    if CHECK_DATA == 1:
        os.chdir(TRAIN_SET_PATH)
        match_image_data = bf.load_image(match_image_name)
        os.chdir(BACK_TO_ROOT_REF)
        matchImageData = {'image': match_image_data, 'name': match_image_name}
        sourceImageData = {'image': source_image_data, 'name': source_image_name}
        bf.show_result(sourceImageData, matchImageData, "Result by Original Algorithm")
    elif CHECK_DATA == 0:
        print("Best Match Image (By Original Algorithm): ", match_image_name)
    
    match_image_name = compareNew(sourceFinalArray)
    if CHECK_DATA == 1:
        os.chdir(TRAIN_SET_PATH)
        match_image_data = bf.load_image(match_image_name)
        os.chdir(BACK_TO_ROOT_REF)
        matchImageData = {'image': match_image_data, 'name': match_image_name}
        sourceImageData = {'image': source_image_data, 'name': source_image_name}
        bf.show_result(sourceImageData, matchImageData, "Result by Improved Matching Algorithm")
    elif CHECK_DATA == 0:
        print("Best Match Image (By Improved Matching Algorithm): ", match_image_name)
    # bf.show_image(query_image_data)
    # print(sourceFinalArray)

def compare(sourceArray):
    global TRAIN_DATA
    score = sys.maxsize
    match = ''
    for key, data in TRAIN_DATA.items():
        diffGrey = math.sqrt(sum([(x1-x2)**2 for (x1,x2) in zip(sourceArray['grey'],data['grey'])]))
        diffShape = math.sqrt(sum([(x1-x2)**2 for (x1,x2) in zip(sourceArray['shape'],data['shape'])]))
        diffTexture = math.sqrt(sum([(x1-x2)**2 for (x1,x2) in zip(sourceArray['texture'],data['texture'])]))
        diffScore = diffTexture + diffShape + diffGrey
        if diffScore < score:
            score = diffScore
            match = data['filename']
            # print(diffGrey, diffShape, diffTexture, diffScore)
    return match

def compareNew(sourceArray):
    global TRAIN_DATA, rangeDiffGrey, rangeDiffTexture, rangeDiffShape
    score = sys.maxsize
    rangeDiffGrey = rangeDiffTexture = rangeDiffShape = 0
    for key, data in TRAIN_DATA.items():
        diffGrey = math.sqrt(stat.mean([(x1-x2)**2 for (x1,x2) in zip(sourceArray['grey'],data['grey'])]))
        diffShape = math.sqrt(stat.mean([(x1-x2)**2 for (x1,x2) in zip(sourceArray['shape'],data['shape'])]))
        diffTexture = math.sqrt(stat.mean([(x1-x2)**2 for (x1,x2) in zip(sourceArray['texture'],data['texture'])]))
        rangeDiffGrey = max(rangeDiffGrey, diffGrey)
        rangeDiffShape = max(rangeDiffShape, diffShape)
        rangeDiffTexture = max(rangeDiffTexture, diffTexture)
    match = ''
    for key, data in TRAIN_DATA.items():
        diffGrey = math.sqrt(stat.mean([(x1-x2)**2 for (x1,x2) in zip(sourceArray['grey'],data['grey'])]))/rangeDiffGrey
        diffShape = math.sqrt(stat.mean([(x1-x2)**2 for (x1,x2) in zip(sourceArray['shape'],data['shape'])]))/rangeDiffShape
        diffTexture = math.sqrt(stat.mean([(x1-x2)**2 for (x1,x2) in zip(sourceArray['texture'],data['texture'])]))/rangeDiffTexture
        diffScore = diffTexture + diffShape + diffGrey
        if diffScore < score:
            score = diffScore
            match = data['filename']
            # print(diffGrey, diffShape, diffTexture, diffScore)
    return match

def getDatasetStatus():
    status = -1
    if os.path.isdir(VALIDATION_SET_PATH) and os.path.isdir(TRAIN_SET_PATH):
        status = 1
    elif os.path.isdir(VALIDATION_SET_PATH):
        status = 0
    return status
    
if __name__ == "__main__":
    main()