# from model import billboard_model_main
from model import billboard_model
from import_images import import_train_images
from tensorflow import random

# import matplotlib.pyplot as plt
trainings_imgs, validation_imgs = import_train_images()
model_save_loc = './trained_models/trained_model_06'
print(model_save_loc, '\n')

def print_import_status(training_imgs, validation_imgs):

    for training_img, training_label in training_imgs:
        numb_train_imgs = training_img.numpy().shape#[0]
        numb_train_class_1 = int(training_label.numpy().sum())
    
    for validation_img, validation_labels in validation_imgs:
        numb_val_imgs = validation_img.numpy().shape#[0]
        numb_val_class_1 = int(validation_labels.numpy().sum()) 

    # Print image stats
    print(f'There are {numb_train_imgs} training images')
    print(f'There are {numb_val_imgs} validation images\n')

    # print(f'There are {numb_train_imgs - numb_train_class_1} training images of class damaged')
    # print(f'There are {numb_train_class_1} training images of class pristine\n')

    # print(f'There are {numb_val_imgs - numb_val_class_1} training images of class damaged')
    # print(f'There are {numb_val_class_1} validation images of class pristine\n')


# print_import_status(trainings_imgs, validation_imgs)

# Train billboard_model
model = billboard_model()

# model.summary()

random.set_seed(1)
history = model.fit(
    trainings_imgs,
    validation_data=validation_imgs,
    epochs=45
)

print('\nTime to save model')
model.save(model_save_loc)
print('Model Saved')


import matplotlib.pyplot as plt
history = history.history

loss = history['loss']
val_loss = history['val_loss']

acc = history['sparse_categorical_accuracy']
val_acc = history['val_sparse_categorical_accuracy']

fig, axes = plt.subplots(2, 1)

axes[0].plot(loss, label='training loss')
axes[0].plot(val_loss, label='validation loss')
axes[0].legend()

axes[1].plot(acc, label='training accuracy')
axes[1].plot(val_acc, label='validation accuracy')
axes[1].legend()

plt.show()