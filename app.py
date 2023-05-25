# # import main Flask class and request object
from flask_cors import CORS
from flask import Flask, request, jsonify
import ps_scrape as ps_scrape
import json
# # create the Flask app
app = Flask(__name__)

# # allow both GET and POST requests

# allow both GET and POST requests
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    # handle the POST request
    if request.method == 'POST':
        p = request.form.get('pw')
        a = request.form.get('act')
        r = request.form.get('req')
        if r == 'grades':
            data = (ps_scrape.aall(p, a))
            return (jsonify(data))
        elif r == 'schedule':
            data = (ps_scrape.getSchedule(p, a))
            if data == "I":
                return "Record not found", 400
            return (jsonify(data))

        # data = (ps_scrape.aall(p, a))
        # return ((json.dumps(data, indent=4)))

    # otherwise handle the GET request
    return '''<form method="POST">
        
        <div>
        <label>username: <input type="username" name="act"></label>
        </div>
        <div>
        <label>password: <input type="password" name="pw"></label>
        </div>
        <select name="req">
        <option value="grades">Grades</option>
        <option value="schedule">Schedule</option>
        <input type="submit" value="Submit">
        </form>
        
 
</select>'''


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)

# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello_geek():
#     return '<h1>Hello from Flask & Docker</h2>'


# if __name__ == "__main__":
#     app.run(debug=True)
