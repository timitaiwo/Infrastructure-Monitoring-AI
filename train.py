from model import billboard_model_1
from import_images import import_images

# import matplotlib.pyplot as plt
train_imgs, validation_imags = import_images()

# Train billboard_model
billboard_model_1().fit(
    train_imgs,
    validation_data=validation_imags,
    epochs=5
)

