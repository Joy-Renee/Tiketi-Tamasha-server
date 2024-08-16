from flask_mail import Mail, Message

mail = None

def init_mail(app):
    """Initialize the Flask-Mail extension with the app."""
    global mail
    mail = Mail(app)

def send_registration_email(email, customer_name, phone_number):
    """Send a registration confirmation email."""
    try:
        msg = Message("Registration Successful",
                      recipients=[email])
        msg.body = f"Hello {customer_name},\n\nThank you for registering!\n\nYour registration details:\nPhone: {phone_number}\nEmail: {email}"
        mail.send(msg)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}











































# from flask import Flask, request, jsonify
# from flask_mail import Mail, Message
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "https://tiketi-tamasha-client-omega.vercel.app/register"}})

# app.config['DEBUG'] = True
# app.config['TESTING'] = False
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587  
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False  
# app.config['MAIL_DEBUG'] = True
# app.config['MAIL_USERNAME'] = 'vikakamau72@gmail.com'
# app.config['MAIL_PASSWORD'] = 'xpsn opvb qggt vicj'
# app.config['MAIL_DEFAULT_SENDER'] = 'vikakamau72@gmail.com'
# app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_ASCII_ATTACHMENTS'] = False

# mail = Mail(app)

# # @app.route('/')
# # def index():
# #     # First Email
# #     msg = Message("Test Email", recipients=["vikakamau04@gmail.com"])
# #     msg.body = "Hello, this is a test email from the Flask-Mail application."
# #     mail.send(msg)

# #     msg = Message(
# #         subject = '',
# #         recipients = [],
# #         body= '',
# #         sender= '',
# #         cc = '',
# #         bcc= '',
# #         attachments= '',
# #         html='',
# #         charset = '',
# #         # headers = '',
# #         reply_to= '',
# #         date = '',
# #         )

# #     return "Email sent successfully!"


# # @app.route('/register', methods=['POST'])
# # def register():
# #     try:
# #         # Get the user details from the request
# #         data = request.get_json()
# #         customer_name = data['customer_name']
# #         email = data['email']
# #         phone_number = data['phone_number']
        
# #         # Logic to save the user data (you would typically save this in a database)
# #         # Assuming the user registration is successful
        
# #         # Send the confirmation email
# #         msg = Message("Registration Successful",
# #                       recipients=[email])
# #         msg.body = f"Hello {customer_name},\n\nThank you for registering!\n\nYour registration details:\nPhone: {phone_number}\nEmail: {email}"
# #         mail.send(msg)
        
# #         # Return success response
# #         return jsonify({"success": True}), 200
# #     except Exception as e:
# #         return jsonify({"success": False, "error": str(e)}), 500


# # if __name__ == "__main__":
# #     app.run()