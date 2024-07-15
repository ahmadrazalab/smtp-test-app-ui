from flask import Flask, render_template, request, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate a secure random secret key

def send_test_email(smtp_server, smtp_port, smtp_user, smtp_password, from_email, to_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "SMTP Test Email"
        body = "This is a test email to verify SMTP credentials."
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        return True, "Test email sent successfully!"
    except Exception as e:
        return False, str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        smtp_server = request.form['smtp_server']
        smtp_port = int(request.form['smtp_port'])
        smtp_user = request.form['smtp_user']
        smtp_password = request.form['smtp_password']
        from_email = request.form['from_email']
        to_email = request.form['to_email']

        success, message = send_test_email(smtp_server, smtp_port, smtp_user, smtp_password, from_email, to_email)
        flash(message, 'success' if success else 'error')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
