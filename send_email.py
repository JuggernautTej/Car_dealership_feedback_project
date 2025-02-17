import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

def send_mail(customer, dealer, rating, comments):
    port = int(os.getenv('MAIL_PORT'))
    smtp_server = os.getenv('MAIL_SERVER')
    login = os.getenv('MAIL_LOGIN')
    password = os.getenv('MAIL_PASSWORD')
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Audi Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
