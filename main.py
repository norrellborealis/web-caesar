from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

rot_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/add" method="POST">
            <label>
                Rotate By:
                <input id="rot" type="text" name="rot"/>
            </label>
        <br />
            <label>
                <input id="text" type="textarea" name="text"/>
            </label>
        <br />
            <input type="submit" value="Submit Query"/>
         </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return rot_form

@app.route("/add", methods=['POST'])
def encrpyt():
    text = request.form.get("text")
    rot = int(request.form.get("rot"))
    rotate_string = caesar.encrypt(text,rot)
    encrypted_message = rotate_string
    return encrypted_message

app.run()