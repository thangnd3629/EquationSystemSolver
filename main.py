import base64
import io
import os
import cv2

import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, url_for, send_file

from flask_cors import CORS
from werkzeug.utils import secure_filename
from solver.set_of_equation_solver import soe_solver

app = Flask(__name__)
CORS(app=app)

app.secret_key = "secret key"

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def encode(img):
    img = cv2.resize(img, (500, 500))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img)
    buff = io.BytesIO()
    pil_img.save(buff, format="JPEG")
    img = base64.b64encode(buff.getvalue()).decode("utf-8")
    return img

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file = request.files['file']
            npimg = np.fromfile(file, np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            detected = soe_solver(img)
            if(detected is not None):
                result, list_text_equation, eqs_cropped, deskewed_img, equation_coor_1 = detected
                for i in equation_coor_1:
                    deskewed_img = cv2.rectangle(deskewed_img, (i[0], i[1]), (i[0] + i[2], i[1] + i[3]),
                                                 (102, 255, 102), 2)







            return ({
                "result":tuple(result),
                "list_eqs":tuple(list_text_equation),
                "original_img":encode(img),
                "deskewed_img":encode(deskewed_img),
                "cropped_eq":encode(eqs_cropped),


            })
        return "OK"
    else:
        return "GET"

if __name__ == "__main__":
    app.run()
