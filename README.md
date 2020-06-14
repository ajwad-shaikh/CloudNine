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

The module contains different python programs that are interdependent for use in the project

- ### base_functions.py
    - Contains basic file I/O functions, especially to deal with h5 type images as received by ISRO Database
- ### analysis.py 
    - Contains analysis functions such as histogram processing, shape and texture analysis to derive the required feature lists that we want to store
- ### process.py
    - Contains a function to process a single image as per algorithm in the paper and generate a feature object
- ### upload.py
    - Contains script to calculate features of train set and upload the results to Firebase Realtime Database

Course - CS313a - Image Processing 
Mentor - Dr. Pritee Khanna
Team - Ajwad Shaikh and Kaushal Sharma
Institute - Indian Institute of Information Technology, Design and Manufacturing, Jabalpur