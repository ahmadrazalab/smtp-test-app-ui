# app.py

from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    smtp_host = request.form['host']
    smtp_port = int(request.form['port'])  # Convert port to integer
    smtp_username = request.form['username']
    smtp_password = request.form['password']
    email_to = request.form['to']
    email_subject = request.form['subject']
    email_body = request.form['body']

    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        message = f"Subject: {email_subject}\n\n{email_body}"
        server.sendmail(smtp_username, email_to, message)
        server.quit()

        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {e}"

#if __name__ == '__main__':
 #   app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')