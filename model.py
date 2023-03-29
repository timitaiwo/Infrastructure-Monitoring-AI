import tensorflow as tf
from keras import Sequential, layers, optimizers, losses, metrics
from import_images import img_width, img_height

# set seed to control randomness
tf.random.set_seed(1)

# Define data augmentation layer
data_aug = Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.3)
])

# Sample Model
num_classes = 2

def billboard_model():
    billboard_model = Sequential([
    layers.Resizing(256, 256),
    layers.Rescaling(1./255),
    data_aug,
    layers.Conv2D(4, (3, 3), padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(4, (3, 3), padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(4, (3, 3), padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(1024, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
    ])

    # Compile the model
    billboard_model.compile(
        optimizer=optimizers.Adam(learning_rate=0.0001),
        loss=losses.SparseCategoricalCrossentropy(),
        metrics=[metrics.SparseCategoricalAccuracy()]
    )

    return billboard_model



#     billboard_model.add(layers.Conv2D(
#         filters=32, kernel_size=(5, 5), strides=(1, 1),
#         padding='same', data_format='channels_last',
#         name='conv_1', activation='relu'
#     ))

#     billboard_model.add(layers.MaxPool2D(
#         pool_size=(2, 2), name='pool 1'
#     ))

#     billboard_model.add(layers.Conv2D(
#         filters=64, kernel_size=(5, 5), strides=(1, 1),
#         padding='same', name='conv_2', activation='relu'
#     ))

#     billboard_model.add(layers.MaxPool2D(
#         pool_size=(2, 2), name='pool_2'
#     ))

#     billboard_model.add(layers.Flatten())

#     billboard_model.add(layers.Dense(
#         units=1024, name='fc_1',
#         activation='relu'
#     ))

#     billboard_model.add(layers.Dropout(
#         rate=0.5
#     ))

#     billboard_model.add(layers.Dense(
#         units=10, name='fc_2',
#         activation='softmax'
#     ))
