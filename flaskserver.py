# import main Flask class and request object
from flask import Flask, request, jsonify
import ps_scrape
# create the Flask app
app = Flask(__name__)

# allow both GET and POST requests


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        p = request.form.get('pw')
        a = request.form.get('act')
        data = (ps_scrape.aall(p, a))
        print(data)
        return str(data)
        # return '''{}+lol+{}'''.format(language, framework)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
