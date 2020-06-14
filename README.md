# CloudNine 
### Search for the clouds!

A Python Implementation for Satellite Cloud Image Processing and Information Retrieval System

## Installation

- `git clone https://github.com/ajwad-shaikh/CloudNine.git`
- `cd CloudNine`
- `virtualenv env`
- `"src/scripts/activate"`
- `pip install -r requirements.txt`

This will install the necessary dependencies for the function scripts.

## Dataset

The Dataset was ordered from [MOSDAC (Meteorological and Oceanographic Satellite Data Archival Centre)](https://www.mosdac.gov.in/) maintained and sourced from Indian Space Research Organization (ISRO) Kalpana Satellite's VHF Sensor. We have 603 satellite images in HDF5 format but due to the bulk size of the dataset, it has not been included in the repository.

To get the project to work, you need the complete or at least part of the database - 
    
1. Download the complete dataset from here -> [dataset.zip](https://drive.google.com/file/d/1wjWE7kmlHOFMN8FYHZd01rhKtsmpvUUh/view?usp=sharing) (890 MB)
    - You can then unpack the archive in `<project_root>/dataset`
    - This will help you run the project full-fledged with the similar images displayed alongside query image from the validation set
2. Download the validation set of images from here -> [validation_set.zip](https://drive.google.com/file/d/12iaBgFLypnFJyy1DCQEjrm5WpckBc6q1/view?usp=sharing) (78 MB)
    - You can then unpack the archive in `<project_root>/dataset/validation_set`
    - This will help you run the project as MVP, but will only return image names of the matched images from train set instead of actual images.

## Scripts in the Module

The module contains different python programs that are interdependent for use in the project

- ### base_functions.py
    - Contains basic file I/O functions, especially to deal with h5 type images as received by ISRO Database
- ### analysis.py 
    - Contains analysis functions such as histogram processing, shape and texture analysis to derive the required feature lists that we want to store
- ### process.py
    - Contains a function to process a single image as per algorithm in the paper and generate a feature object
- ### upload.py
    - Contains script to calculate features of train set and upload the results to Firebase Realtime Database

## Feature Database

We have computed and uploaded features of all images in the training set (550 images) to a Firebase Realtime Database. You can view the feature database here -> [Link to Database](https://odk-x-push.firebaseio.com/cloudNine.json)

Course - CS313a - Image Processing 
Mentor - Dr. Pritee Khanna
Team - [Ajwad Shaikh](https://ajwad-shaikh.github.io) and Kaushal Sharma
Institute - Indian Institute of Information Technology, Design and Manufacturing, Jabalpur