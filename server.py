from os import statvfs_result
import csv
from flask import Flask, render_template
from flask import request, redirect
app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return render_template('./index.html')
@app.route("/about.html")
def orld():
    return render_template('./about.html')
# @app.route("/favicon.ico")
# def blog ():
#     return "<h1>Peace!</h1>"
@app.route("/blog/2020/dogs")
def dogs ():
    return "<h1>Peace! is not piegon</h1>"
# @app.route("/<username>")
# def hello( username = None):
#     return render_template('index.html', name=username)
@app.route("/components.html")
def rld():
    return render_template('./components.html')
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('databasepython.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email} , {subject} ,{message}')
def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])
@app.route("/contact.html")
def orvhld():
    return render_template('./contact.html')
@app.route("/work.html")
def gorld():
    return render_template('./work.html')
@app.route("/works.html")
def eorld():
    return render_template('./works.html')
@app.route("/index.html")
def eorlgd():
    return render_template('./index.html')
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            write_to_file(data)
            return render_template('./thankyou.html')
        except :
            return "did not save to database"
        else:
            return'try again'


