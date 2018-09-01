#!flask/bin/python
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.datastructures import FileStorage
import pickle

import numpy as np
from PIL import Image
from scipy.misc.pilutil import fromimage
from scipy.misc import imresize

app = Flask(__name__)
api = Api(app)


kids = {
    'Sean': 'Professional iPad breaker.',
    'Jerry': 'Likes memes and plays orchestra.',
    'Sophia': 'Unicorn! Awesome! Amazing! A+! A VIP!'
}

def read_jpg(file_path):
    image = Image.open(file_path)
    if hasattr(image, '_getexif'):
        orientation = 0x0112
        exif = image._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotations:
                image = image.transpose(rotations[orientation])

    img = fromimage(image, flatten=False, mode=None)
    # convert to gray-scale image
    img = img.mean(axis=2)
    return np.asarray(img, dtype=np.float32)


def load_one_face(face, resize = 250, slice_=(slice(70, 195), slice(78, 172))):
    if resize is not None:
        face = imresize(face, (resize, resize))
        face = np.asarray(face[slice_], dtype=np.float32)

    return face


class CodeName(Resource):
    def get(self, name=None):
        if name is None or name == 'all':
            return kids
        else:
            if name not in kids:
                abort(404, message='I have not heard of' + name)
            return {name: kids[name]}

    def save_the_pickle(self):
        output = open('data.pkl', 'wb')
        pickle.dump(kids, output)
        output.close()

    def post(self):
        json_data = request.get_json(force=True)
        name = json_data['name']
        action = json_data.get('action')
        if action == 'delete' and name in kids:
            del kids[name]
            self.save_the_pickle()
            return kids, 201
        elif action == 'update':
            code_name = json_data['code_name']
            kids[name] = code_name
            self.save_the_pickle()
            return kids[name], 201
        else:
            return 'What in the worldy world r u trying to doooo????????', 404


class FaceClassifier(Resource):
    def predict_face(self, img):
        some_face = load_one_face(img, resize=250, slice_=(slice(0, 250), slice(0, 210)))
        pkl_file = open('/models/data.pkl', 'rb')
        face_model = pickle.load(pkl_file)
        pkl_file.close()
        names_file = open('/models/names.pkl', 'rb')
        target_names = pickle.load(names_file)
        names_file.close()

        predicted_label = face_model.predict([some_face.flatten()])[0]

        return target_names[predicted_label]

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('photo', type=FileStorage, location='files')
        args = parse.parse_args()
        stream = args['photo'].stream
        img = read_jpg(stream)

        return {'predicted_face': self.predict_face(img)}


api.add_resource(CodeName, '/', '/<name>')
api.add_resource(FaceClassifier, '/whoisit')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
