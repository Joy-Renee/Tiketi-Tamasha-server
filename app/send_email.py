from flask import current_app
from flask_mail import Mail, Message

mail = Mail()

def send_registration_email(customer):
    try:
        msg = Message(
            'Registration Successful',
            sender=current_app.config['MAIL_USERNAME'],
            recipients=[customer.email]
        )
        msg.body = f'''
        Hi {customer.customer_name},

        Your registration was successful!

        You can log in using the following link:
        http://your-domain.com/login

        Thank you,
        Your Company
        '''
        mail.send(msg)
    except Exception as e:
        # Log the exception or handle it as needed
        print(f"Failed to send email: {e}")
