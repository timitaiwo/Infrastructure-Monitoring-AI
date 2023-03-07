# Image capture library
import cv2

# Path management libraries
from pathlib import Path
from shutil import rmtree

# Time management library
from datetime import datetime, timedelta


# Program
def five_sec_image_capture():
    '''
    main function of image_capture.py

    '''
    desired_dir = ensure_location_exists()

    if desired_dir != None:
        rolling_capture(desired_dir)
    else:
        print('Program can\'t run as temporary folder to store image cannot be created')

    return None


def rolling_capture(desired_dir):
    '''
    Runs the function to capture images every five seconds.
    '''

    trigger_time = datetime.now().replace(microsecond=0)


    while True:

        if trigger_time == datetime.now().replace(microsecond=0):
            save_image(desired_dir)

        else:
            continue
        
        time_now = datetime.now().replace(microsecond=0)
        five_secs = five_secs_later(time_now)
        trigger_time = five_secs

    return None


def save_image(file_location):
    '''
    Save the image when 
    '''

    # assert file_location == ensure_location_exists()

    print('filler function')
    

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
    five_sec_image_capture()