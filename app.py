# # import main Flask class and request object
from flask import Flask, request
import ps_scrape as ps_scrape
# # create the Flask app
app = Flask(__name__)

# # allow both GET and POST requests

# allow both GET and POST requests


@app.route('/', methods=['GET', 'POST'])
def home():
    # handle the POST request
    if request.method == 'POST':
        p = request.form.get('pw')
        a = request.form.get('act')
        data = (ps_scrape.aall(p, a))
        # print(data)
        return ((str(data)))

    # otherwise handle the GET request
    return '''<form method="POST"><div><label>psw: <input type="text" name="pw"></label></div><div><label>act: <input type="text" name="act"></label></div><input type="submit" value="Submit"></form>'''


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5003)

# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello_geek():
#     return '<h1>Hello from Flask & Docker</h2>'


# if __name__ == "__main__":
#     app.run(debug=True)
