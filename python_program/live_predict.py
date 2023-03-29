# Image capture library
import cv2
from tensorflow import constant, newaxis
from numpy import argmax
import tensorflow as tf

# Path management libraries
from pathlib import Path
from shutil import rmtree

# Time management library
from datetime import datetime, timedelta

# import ML model
from keras.models import load_model
model = load_model('trained_model_05')
print('\nModel loaded\n')
classes = {0:'damaged', 1:'pristine'}


# Program
webcam = cv2.VideoCapture(0)


def main():
    '''
    main function of image_capture.py

    '''
    desired_dir = ensure_location_exists()

    if desired_dir != None:
        rolling_capture()
    else:
        print('Program can\'t run as temporary folder to store image cannot be created')

    return None


def rolling_capture():
    '''
    Runs the function to capture images every five seconds.
    '''

    trigger_time = datetime.now().replace(microsecond=0)

    print('Image Capture begins')

    while True:

        if trigger_time == datetime.now().replace(microsecond=0):
            capture_image_and_predict()

        else:
            continue
        
        time_now = datetime.now().replace(microsecond=0)
        five_secs = five_secs_later(time_now)
        trigger_time = five_secs


def capture_image_and_predict():
    '''
    Save the image and run the AI model on image
    '''

    if webcam.isOpened():
        # Capture Image
        _, footage = webcam.read()
        footage = cv2.cvtColor(footage, cv2.COLOR_BGR2GRAY)
        file_name = f'./captured_images/{datetime.now().replace(microsecond=0)}.jpg'.replace(':', '')
        cv2.imwrite(file_name, footage)

        # Make prediction
        footage = constant(footage)
        footage = footage[newaxis, ..., newaxis]
        footage = tf.image.resize_with_pad(footage, 256, 256)
        prediction = model.predict(footage)
        pred_class = argmax(prediction)
        print(f'{datetime.now().replace(microsecond=0)}: The class is {classes[pred_class]}')
        # cv2.waitKey('25')
    
    else:
        print('webcam not connected')

    return None


def ensure_location_exists():
    '''
    Ensure that captured_images exists, else create it
    '''

    main_dir = Path.cwd()

    desired_directory_name = 'captured_images'
    desired_directory = main_dir.joinpath(desired_directory_name)

    # Check if desired directory exists and delete if so
    if desired_directory.exists() and desired_directory.is_dir():
        print(f'\n"{desired_directory_name}" directory exists')
        print('deleting...\n')

        rmtree(desired_directory)

        print('deleted...') if not desired_directory.exists() else None
        print('recreating directory')

        desired_directory.mkdir()

    elif not desired_directory.exists():
        print(f'\n{desired_directory_name} does not exist')
        print('creating...\n')

        desired_directory.mkdir()
    
    if desired_directory.exists() and desired_directory.is_dir():
        print(f'\nThe directory \n\n{desired_directory} \n\nis created\n')
    else:
        print(f'The directory is not created/recreated')
        return None
        

    return desired_directory


def five_secs_later(time_now=datetime.now()):
    '''
    Returns the value of time in 5 seconds
    '''
    five_secs_later = time_now + timedelta(seconds=5)
    return five_secs_later.replace(microsecond=0)


if __name__=='__main__':
    main()