# Import libraries
from tensorflow import random
from keras.utils import image_dataset_from_directory
from keras import Sequential, layers


import matplotlib.pyplot as plt
import numpy as np

# set randomness
random.set_seed(1)

# Set import params
batch_size = 32
img_width = 256
img_height = 256


def import_train_images():
    '''
    Import images to tensorflow dataset 
    '''
    print('\n')
    try:
        img_dir  = './training_images/normal_imgs'
        train_imgs = image_dataset_from_directory(img_dir,
                                                    validation_split=0.2,
                                                    subset='training',
                                                    seed=1,
                                                    image_size=(img_height, img_width),
                                                    label_mode='binary', color_mode='grayscale',
                                )
        print('Printed Number of Images for Training\n')

        validation_imgs = image_dataset_from_directory(img_dir,
                                                    validation_split=0.2,
                                                    subset='validation',
                                                    seed=1,
                                                    image_size=(img_height, img_width),
                                                    label_mode='binary', color_mode='grayscale',
                                )
        print('Printed Number of Images for Validation\n')

        imgs_imported = True
        print('All Images imported\n')

    except Exception as exception:
        print(f'\nimage_import failed: {exception}\n')
        imgs_imported = False

    if imgs_imported:
        train_imgs = train_imgs.shuffle(buffer_size= 3)
        validation_imgs = validation_imgs.shuffle(buffer_size= 3)
        return train_imgs, validation_imgs
    else:
        return None, None


def import_test_images():
    '''
    Import images to tensorflow dataset 
    '''
    print('\n')
    try:
        test_img_dir  = './training_images/test_imgs'
        test_imgs = image_dataset_from_directory(test_img_dir,
                                                    image_size=(img_height, img_width),
                                                    batch_size=batch_size,
                                                    label_mode='binary', color_mode='grayscale',
                                )
        print('Printed Number of Images for Test\n')

        imgs_imported = True
        print('All Images imported\n')

    except Exception as exception:
        print(f'\nimage_import failed: {exception}\n')
        imgs_imported = False

    if imgs_imported:
        test_imgs = test_imgs.shuffle(buffer_size= 3)
        return test_imgs
    else:
        return None


def test_img_import(img_datset):

    for images, labels in img_datset:
        train_imgs = images.numpy()
        train_labels = labels.numpy()

    # test = train_imgs[1, :, :]

    # print(train_labels[1])
    # plt.imshow(test, cmap='gray')
    # plt.show()

    num_imgs = train_imgs.shape[0]
    fig, axes = plt.subplots(1, num_imgs)

    for img in range(num_imgs):
        axes[img].imshow(train_imgs[img, :, :], cmap='gray')
        axes[img].text(2, 2, train_labels[img])

    plt.show()
    return None


if __name__ == '__main__':
    imgs_data, validation_data = import_train_images()
    test_data = import_test_images()

    if imgs_data != None and validation_data != None:
        test_img_import(imgs_data)
