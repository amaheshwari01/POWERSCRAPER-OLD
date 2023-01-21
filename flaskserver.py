# # import main Flask class and request object
from flask import Flask, request, jsonify
import ps_scrape as ps_scrape
# # create the Flask app
app = Flask(__name__)

# # allow both GET and POST requests


# @app.route('/form-example', methods=['GET', 'POST'])
# def form_example():
#     # handle the POST request
#     if request.method == 'POST':
#         p = request.form.get('pw')
#         a = request.form.get('act')
#         data = (ps_scrape.aall(p, a))
#         print(data)
#         return str(data)
#     return '''
#            <form method="POST">
#                <div><label>Language: <input type="text" name="language"></label></div>
#                <div><label>Framework: <input type="text" name="framework"></label></div>
#                <input type="submit" value="Submit">
#            </form>'''


# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        p = request.form.get('pw')
        a = request.form.get('act')
        data = (ps_scrape.aall(p, a))
        # print(data)
        return str(data)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>psw: <input type="text" name="pw"></label></div>
               <div><label>act: <input type="text" name="act"></label></div>
               <input type="submit" value="Submit">
           </form>'''


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
