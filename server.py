import os
from flask import Flask, render_template, request, redirect
import resend
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#.env file
resend.api_key = os.getenv('RESEND_API_KEY') 

@app.route('/')
def my_home():
    return render_template('index.html')
#routing all pages
@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name)
    except Exception:
        return render_template('404.html'), 404

#send email through request
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            user_name = data.get('name', 'Anonymous')
            user_email = data.get('email', 'No Email Provided')
            user_msg = data.get('message', 'No Message Content')


            params = {
                "from": "onboarding@resend.dev",
                "to": "chanchunkiu2001@gmail.com", 
                "subject": f"New Portfolio Message from {user_name}",
                "text": f"Name: {user_name}\nEmail: {user_email}\nMessage: {user_msg}"
            }
            
            resend.Emails.send(params)

            return redirect('/thankyou.html')
        except Exception as e:
            print(f"Error: {e}") 
            return 'Something went wrong. Please try again later.'

    return 'Method not allowed'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
