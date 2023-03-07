# check if last processed image is latest available.
# Process image is last processed image is not latest available


# Path management library
from pathlib import Path


def parse_latest_image():
    location = ensure_location_exists()
    
    if location == None:
        raise Exception('The Directory \'captured_images\' is Missing')
    




def ensure_location_exists():
    '''
    Ensure that captured_images exists, else create it
    '''

    main_dir = Path.cwd()

    desired_directory_name = 'captured_images'
    desired_directory = main_dir.joinpath(desired_directory_name)

    # Check if desired directory exists else return None
    if desired_directory.exists() and desired_directory.is_dir():
        print(f'\n"{desired_directory_name}" directory exists')
        return desired_directory

    elif not desired_directory.exists():
        print(f'\n{desired_directory_name} directory does not exist\n')
        return None


if __name__ == '__main__':
    parse_latest_image()