import tensorflow as tf
from keras import Sequential, layers, optimizers, losses

# set seed to control randomness
tf.random.set_seed(1)



def billboard_model_main():
    # Define the CNN model
    billboard_model = Sequential()

    # Add Normalizaion Layer
    billboard_model.add(layers.Rescaling(1./255))

    billboard_model.add(layers.Conv2D(
        filters=32, kernel_size=(5, 5), strides=(1, 1),
        padding='same', data_format='channels_last',
        name='conv_1', activation='relu'
    ))

    billboard_model.add(layers.MaxPool2D(
        pool_size=(2, 2), name='pool 1'
    ))

    billboard_model.add(layers.Conv2D(
        filters=64, kernel_size=(5, 5), strides=(1, 1),
        padding='same', name='conv_2', activation='relu'
    ))

    billboard_model.add(layers.MaxPool2D(
        pool_size=(2, 2), name='pool_2'
    ))

    billboard_model.add(layers.Flatten())

    billboard_model.add(layers.Dense(
        units=1024, name='fc_1',
        activation='relu'
    ))

    billboard_model.add(layers.Dropout(
        rate=0.5
    ))

    billboard_model.add(layers.Dense(
        units=10, name='fc_2',
        activation='softmax'
    ))

    billboard_model.build((None, 256, 256, 1))
    billboard_model.summary()

    # Compile the model 
    billboard_model.compile(
        optimizer=optimizers.Adam(),
        loss=losses.BinaryCrossentropy(),
        metrics=['accuracy']
    )

    return billboard_model



# # Sample Model
# num_classes = 2

# billboard_model = tf.keras.Sequential([
#   tf.keras.layers.Rescaling(1./255),
#   tf.keras.layers.Conv2D(32, 3, activation='relu'),
#   tf.keras.layers.MaxPooling2D(),
#   tf.keras.layers.Conv2D(32, 3, activation='relu'),
#   tf.keras.layers.MaxPooling2D(),
#   tf.keras.layers.Conv2D(32, 3, activation='relu'),
#   tf.keras.layers.MaxPooling2D(),
#   tf.keras.layers.Flatten(),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dense(num_classes)
# ])

# # Compile the model
# billboard_model.compile(
#     optimizer=optimizers.Adam(),
#     loss=losses.BinaryCrossentropy(),
#     metrics=['accuracy']
# )