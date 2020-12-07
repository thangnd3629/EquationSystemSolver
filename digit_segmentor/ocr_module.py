from preprocess.preprocess import preprocessing_image

from tensorflow.keras.models import load_model
import numpy as np
import config

ocr_path = config.ocr_path
print(ocr_path)
model = load_model(ocr_path)
names = ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', 'a', 'b', 'c', 'd', 'x', 'y', 'z']


def ocr(list_image):
    eq_str = ""
    for image in list_image:
        preprocess_image = preprocessing_image(image)
        y_predict = model.predict(preprocess_image.reshape(1, 28, 28, 1))
        text_predict = names[np.argmax(y_predict)]

        if np.max(y_predict) >= 0.5:
            eq_str += text_predict
    return eq_str
