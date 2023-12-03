import flask
from flask import Flask
from flask import request
import PIL
from PIL import Image
import io
from io import StringIO
import base64
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True  # https://stackoverflow.com/questions/42462431/oserror-broken-data-stream-when-reading-image-file

app = Flask(__name__)

@app.route("/")
def home():
    return 'lol'

@app.route("/api")
def api():
    image = Image.open(io.BytesIO(base64.b64decode(request.args.get('base64').replace(' ', '+'))))
    img_io = io.BytesIO()  # https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser
    image.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return flask.send_file(img_io, mimetype='image/jpeg')

