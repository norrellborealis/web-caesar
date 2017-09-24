from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

rot_form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/add" method="POST">
            <label>
                Rotate By:
                <input id="rot" type="text" name="rot" value="0"/>
                <p class="error"></p>
            </label>
            <label>
                <textarea type="text" name="text">{0}</textarea>
            </label>
        <br />
            <input type="submit" value="Submit Query"/>
         </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return rot_form.format("")

@app.route("/add", methods=['POST'])
def encrpyt():
    text = request.form.get("text")
    rot = int(request.form.get("rot"))
    encrypted = rotate_string(text,rot)

    return rot_form.format(encrypted)

app.run()