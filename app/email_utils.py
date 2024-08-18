from flask_mail import Mail, Message



def init_mail(app):
    """Initialize the Flask-Mail extension with the app."""
    global mail
    mail = Mail(app)

def send_registration_email(email, customer_name, phone_number):
    """Send a registration confirmation email with a link to the login page."""
    try:
        msg = Message("Registration Successful",
                      recipients=[email])
        
        # Construct the email body with a link to the login page
        msg.html = f"""
        <p>Hello {customer_name},</p>
        <p>Thank you for registering!</p>
        <p>Your registration details:</p>
        <ul>
            <li>Phone: {phone_number}</li>
            <li>Email: {email}</li>
        </ul>
        <p>Please <a href="https://tiketi-tamasha-client-omega.vercel.app/login">click here to login</a>.</p>
        <p>Thank you!</p>
        """

        mail.send(msg)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
    
def send_registration_email_organizer(email, organizer_name, phone_number):
    """Send a registration confirmation email with a link to the login page."""
    try:
        msg = Message("Registration Successful",
                      recipients=[email])
        
        # Construct the email body with a link to the login page
        msg.html = f"""
        <p>Hello {organizer_name},</p>
        <p>Thank you for registering!</p>
        <p>Your registration details:</p>
        <ul>
            <li>Phone: {phone_number}</li>
            <li>Email: {email}</li>
        </ul>
        <p>Please <a href="https://tiketi-tamasha-client-omega.vercel.app/loginOrganizer">click here to login</a>.</p>
        <p>Thank you!</p>
        """

        mail.send(msg)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
    
def send_event_reminder_email(email, customer_name, event_name, event_date):
    """Send a reminder email about an upcoming event."""
    try:
        msg = Message("Event Reminder: 6 Days to Go!",
                      recipients=[email])
        
        # Construct the email body
        msg.html = f"""
        <p>Hello {customer_name},</p>
        <p>This is a reminder that the event you purchased tickets for, <strong>{event_name}</strong>, is happening on <strong>{event_date.strftime('%B %d, %Y')}</strong>.</p>
        <p>We look forward to seeing you there!</p>
        <p>Thank you for choosing us!</p>
        """

        mail.send(msg)
        print(f"Reminder sent to {email} for event {event_name}.")
        return {"success": True}
    except Exception as e:
        print(f"Failed to send reminder to {email}. Error: {str(e)}")
        return {"success": False, "error": str(e)}











































