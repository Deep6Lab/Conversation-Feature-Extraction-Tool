from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
from flask import request
import json
import time
import datetime
from diarization import diarization
from werkzeug.utils import secure_filename
import os
import asyncio

UPLOAD_FOLDER = 'C:/Users/alish/OneDrive/Desktop/UniversityProjects/ResearchProject/ConvModAPI/uploads'
ALLOWED_EXTENSIONS = {'wav','awb','m4a','mp3','mp4'}
app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class ConvModAPI(Resource):
    def get(self):

        try:
            data = diarization().callSpeechAPI()


        except ValueError:
            print("Oops!  That was no valid number.  Try again...", ValueError)
        return json.loads(data)

    def post(self):
        form = request.form
        print(form.to_dict(self))

        try:
            if 'file' not in request.files:
                return {"file":"Please add file"}, 400
                # If the user does not select a file, the browser submits an
                # empty file without a filename.
            file = request.files['file']
            if file.filename == '':
                return {"file":"Please add file"}, 400

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                data = diarization().callSpeechAPI(filename, form.to_dict(self))
                print(data)
                feature_exraction().extracting_speaker_diarization(data)
                #return redirect(url_for('download_file', name=filename))



        except ValueError:
            print("Oops!  That was no valid number.  Try again...", ValueError)
        return {"data" : json.loads(data)},200

api.add_resource(ConvModAPI, '/app')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
