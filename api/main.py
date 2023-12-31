import base64
import io

import flask
from PIL import Image, ImageFile
from flask import Flask
from flask import request

ImageFile.LOAD_TRUNCATED_IMAGES = True  # https://stackoverflow.com/questions/42462431/oserror-broken-data-stream-when-reading-image-file

app = Flask(__name__)


@app.route("/")
def home():
    return 'lol'


@app.route("/api/<string:base>")
def api(base):
    image = Image.open(io.BytesIO(base64.b64decode(base.replace(' ', '+').replace('_+_+', '/'))))
    img_io = io.BytesIO()  # https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser
    image.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return flask.send_file(img_io, mimetype='image/jpeg')
