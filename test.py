from keras.models import load_model
from numpy import argmax
from pandas import DataFrame
from import_images import import_test_images

from sklearn.metrics import confusion_matrix

# Model Location
model_loc = './trained_models/trained_model_05'

# Test Images
test_imgs = import_test_images()

for images, labels in test_imgs:
    images = images
    test_labels = labels

# Load the saved model
model = load_model(model_loc)
print('Model loaded\n')

model.summary()
scores = model.predict(test_imgs)
pred_vals = argmax(scores, axis=1)

acc_matix = {
    'actual_value': labels.numpy().tolist(),
    'predicted_value': pred_vals
}
actual_pred = DataFrame.from_dict(acc_matix, orient='index')
print(actual_pred)

print(confusion_matrix(labels.numpy().tolist(), pred_vals))

print('\n')
# print(scores, '\n')
# print(pred_vals)
# print(labels.numpy().T)