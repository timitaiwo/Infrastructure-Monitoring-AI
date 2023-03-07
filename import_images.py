# Import libraries
import tensorflow as tf
from keras.utils import image_dataset_from_directory

import matplotlib.pyplot as plt
import numpy as np

# set randomness
tf.random.set_seed(1)

# Set import params
batch_size = 32
img_width = 256
img_height = 256


def import_images():
    '''
    Import images to tensorflow dataset
    '''
    try:
        img_dir  = './training_images/edge_imgs'
        # img_dir  = './training_images/normal_imgs'
        imgs_data = image_dataset_from_directory(img_dir,
                                                    validation_split=0.2,
                                                    subset='training',
                                                    seed=1,
                                                    image_size=(img_height, img_width),
                                                    batch_size=batch_size,
                                                    label_mode='binary', color_mode='grayscale',
                                )
        
        validation_data = image_dataset_from_directory(img_dir,
                                                    validation_split=0.2,
                                                    subset='validation',
                                                    seed=1,
                                                    image_size=(img_height, img_width),
                                                    batch_size=batch_size,
                                                    label_mode='binary', color_mode='grayscale',
                                )

        imgs_imported = True
        print('Images imported')

    except Exception as exception:
        print(f'\nimage_import failed: {exception}\n')
        imgs_imported = False

    if imgs_imported:
        return imgs_data, validation_data
    else:
        return None, None


def test_img_import(imgs_data, validation_data):

    for images, labels in imgs_data:
        train_imgs = images.numpy()
        train_labels = labels.numpy()

    test = train_imgs[1, :, :]

    print(np.min(test), np.max(test))

    # print(train_labels[1])
    # plt.imshow(test, cmap='gray')
    # plt.show()

    return None


if __name__ == '__main__':
    imgs_data, validation_data = import_images()

    if imgs_data != None and validation_data != None:
        test_img_import(imgs_data, validation_data)
