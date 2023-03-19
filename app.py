from flask import Flask, render_template, jsonify, url_for
from flask import request, redirect
from flask_mail import Mail,Message
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'myemail'
app.config['MAIL_PASSWORD'] = 'xxxxxxxxxxx'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
# this app will accept post request with JSON object
# json format = {"receivers":["", ""], "body":"", "subject":"", "bodyType":"html/text"}

@app.route("/", methods=['POST'])
@cross_origin(supports_credentials=True)
def hello_world():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json_f = request.json
            body_f = json_f["body"]
            receivers_f = json_f["receivers"]
            subject_f = json_f["subject"]
            print(receivers_f)
            print(json_f)
            body_type = json_f.get("bodyType", "text")

            if body_type == "html":
                msg = Message(
                    subject_f,
                    sender='vinaydangodra28@gmail.com',
                    recipients=receivers_f,
                    html=body_f
                )
            else:
                msg = Message(
                    subject_f,
                    sender='vinaydangodra28@gmail.com',
                    recipients=receivers_f,
                    body=body_f
                )
            mail.send(msg)
            return "sent"
        else:
            return 'Content-Type not supported!'
    return redirect(request.url)


# if __name__ == "__main__":
#     app.run(port="5000")