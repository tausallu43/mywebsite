import flask
from flask import request, render_template, flash
from dotenv import load_dotenv, find_dotenv
import os
import smtplib

from email.message import EmailMessage


load_dotenv(find_dotenv())
app = flask.Flask(__name__, template_folder="templates/")
app.config["DEBUG"] = True
app.config["UPLOAD_FOLDER"] = "static/"
app.secret_key = '123456789@tousif'


# home page
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


# about_me page
@app.route('/about_me', methods=['POST', 'GET'])
def about_me():
    return render_template('about_me.html')


# call page
@app.route('/call', methods=['POST', 'GET'])
def call():
    return render_template('call.html')


# call_res page
@app.route('/call_res', methods=['POST', 'GET'])
def call_res():
    msg = "############## Contact Details and preferred time : ###############" + '\n'
    Fname = request.form.get('firstname')
    Lname = request.form.get('lastname')
    phone = request.form.get('phone')
    days = request.form.getlist('day')
    print(type(len(days)))
    time = request.form.getlist('time')
    print(str(phone).find("+"))
    body = request.form.get('purpose')

    # whole form validation check point
    if Fname == "" or str(Lname) == "" or str(phone) == "" or str(phone).find("+") == -1  or body == "":
        error = "Please fill the all inputs of the form correctly as instructed."
        flash(error)
    elif len(days) == 0 or len(
            time) == 0:
        error = "Please provide the preferred days and time to call you back."
        flash(error)


    else:
        data = "First Name =  {name}" + '\n' + "Last Name = {lname}" + '\n' + "phone = {phone} \n" + "days = {days} \n" + "time = {time} \n" + '\n' + '\n'
        msg1 = "################ purpose : ###############" + '\n'
        message = msg + data.format(name=Fname, lname=Lname, phone=phone, days=days, time=time) + msg1 + body
        # creates SMTP session

        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(os.getenv("mail"), os.getenv("pass"))

        mail_msg = EmailMessage()
        mail_msg.set_content(message)
        mail_msg['Subject'] = "Request a call back by " + Fname
        mail_msg['From'] = os.getenv("mail")
        mail_msg['To'] = os.getenv("send")

        # sending the mail

        s.send_message(mail_msg)

        # terminating the session
        s.quit()
        flash("Your request has been sent successfully. Thank you so much for your request. I will get back to you soon.")
    return render_template('call.html')


# mail page
@app.route('/mail', methods=['POST', 'GET'])
def mail():
    return render_template('mail.html')


# mail_res page
@app.route('/mail_res', methods=['POST', 'GET'])
def mail_res():
    msg = "############## Contact Details : ###############" + '\n'
    Fname = request.form.get('firstname')
    Lname = request.form.get('lastname')
    mail = request.form.get('mail')
    subject = request.form.get('subject')
    body = request.form.get('message')

    # whole form validation check point
    if Fname == "" or str(Lname) == "" or mail == "" or subject == "" or body == "":
        error = "Please fill the all inputs of the form correctly as instructed."
        flash(error)


    else:
        data = "First Name =  {name}" + '\n' + "Last Name = {lname}" + '\n' + "Mail-ID = {mail}" + '\n' + '\n'
        msg1 = "################ message : ###############" + '\n'
        message = msg + data.format(name=Fname, lname=Lname, mail=mail) + msg1 + body
        # creates SMTP session

        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(os.getenv("mail"), os.getenv("pass"))

        mail_msg = EmailMessage()
        mail_msg.set_content(message)
        mail_msg['Subject'] = subject
        mail_msg['From'] = os.getenv("mail")
        mail_msg['To'] = os.getenv("send")

        # sending the mail

        s.send_message(mail_msg)

        # terminating the session
        s.quit()
        flash(
            "Your request has been sent successfully. Thank you so much for your request. I will get back to you soon.")
    return render_template('mail.html')


# professional page
@app.route('/professional', methods=['POST', 'GET'])
def professional():
    return render_template('professional.html')


# academics page
@app.route('/academics', methods=['POST', 'GET'])
def academics():
    return render_template('academics.html')
# call page
@app.route('/s_success', methods=['POST', 'GET'])
def s_success():
    return render_template('success.html')

# runing the application
if __name__ == '__main__':
    app.run()
