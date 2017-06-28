import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(sender, recipient, subject, body, smtp_host='localhost'):
	message = MIMEMultipart('alternative')
	message['From'] = sender
	message['To'] = recipient
	message['Subject'] = subject
	textPart = MIMEText(body, 'plain')
	message.attach(textPart)

	smtp_server = smtplib.SMTP(smtp_host)
	smtp_server.sendmail(sender, recipient, message.as_string())
