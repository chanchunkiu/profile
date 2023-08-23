import os
from flask import Flask,render_template,send_from_directory,request,redirect
import csv


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/Aboutme.html')
def aboutme():
    return render_template('AboutMe.html')

@app.route('/portfolio.html')
def profile():
    return render_template('portfolio.html')

@app.route('/contactme.html')
def contact():
    return render_template('contactme.html')





@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'failed to save to database'
        else:
            return 'error occur, please try again'



def write_to_file(data):
    with open('database.txt',mode='a') as database:
        name = data['name']
        email = data["email"]
        message= data['message']
        file = database.write(f'\n{name},{email},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data['name']
        email = data["email"]
        message = data['message']
        
        csv_writer = csv.writer(database2, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])