# Pseudocode
# Import necessary modules for email and SSL.
# Define the sender's email address.
# Define the sender's email password.
# Define the receiver's email address.
# Define the email subject.
# Define the email body.
# Create an email message object.
# Set the 'From' field with the sender's email address.
# Set the 'To' field with the receiver's email address.
# Set the 'Subject' field with the email subject.
# Set the content of the email with the email body.
# Create a default SSL context.
# Connect to Gmail's SMTP server using SSL.
# Log in to the SMTP server with the sender's email address and password.
# Send the email using the email message object.
# Print a success message indicating the email was sent successfully.



from email.message import EmailMessage
import ssl
import smtplib

# Setup your email details
email_sender = 'niadavislad@gmail.com'
email_password = 'dcvv rcpg gfhl hovj'  # Use app-specific password or environment variable in production
email_receiver = 'notokaybcmiley1123@gmail.com'  # Set the receiver's email address

subject = "Nia Davis - Python Email Sender Project"
body = "I created an Automated Email Sender using Python. This project streamlines the process of sending emails."

# Create an EmailMessage object
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Setup the SSL context
context = ssl.create_default_context()

# Connect to Gmail's SMTP server in SSL mode
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)  # Log in to the SMTP server
    smtp.send_message(em)  # Send the email

print("Email sent successfully!")
