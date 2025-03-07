import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, jsonify
def send_email(subject, body, to_email):
    from_email = "saimalam843@gmail.com"  
    password = "mkfurajuqmdrvmld"  

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Secure the connection
    server.login(from_email, password)  # Login to Gmail
    text = msg.as_string()  # Convert the email to a string
    server.sendmail(from_email, to_email, text)  # Send the email
    server.quit()  # Disconnect from the server

app = Flask(__name__)


@app.route('/')
def home():
    send_email(
        subject="Deployment Successful",
        body="Your Flask app was deployed successfully!",
        to_email="i211183@nu.edu.pk"  
    )
    return jsonify({"message": "Welcome to the Flask App!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
