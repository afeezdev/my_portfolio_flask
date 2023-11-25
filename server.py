from flask import Flask, render_template, url_for, request, redirect
import csv
from sms_mail  import send_mail

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#write to text file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

#write to csv
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if (data["email"] and data["subject"]) or data["message"]!= '':
                write_to_csv(data)
                send_mail(data)
                return redirect('/thankyou.html')
            else:
                return '<h1>Ooops!!!, you can not leave the email and message empty</h1>'
        except:
            return 'did not save to database'
    else:
        return 'something went wrong.try againa'