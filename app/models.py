from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String)

    bookings = db.relationship('Booking', back_populates='customer', cascade='all, delete-orphan')
    

    def __repr__(self):
        return f'<Customer {self.id}, {self.customer_name}, {self.email}, {self.phone_number}, {self.password}>'

class Ticket(db.Model, SerializerMixin):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    ticket_description = db.Column(db.String)
    ticket_price = db.Column(db.Integer)
    ticket_type = db.Column(db.String)
    available = db.Column(db.Integer)

    # event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    # event = db.relationship('Event', back_populates='tickets')
    bookings = db.relationship('Booking', back_populates='ticket', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Ticket {self.id}, {self.ticket_description}, {self.ticket_price}, {self.ticket_type}, {self.available}>'
    
class Booking(db.Model, SerializerMixin):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    booking_date = db.Column(db.String)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    ticket = db.relationship('Ticket', back_populates='bookings')
    customer = db.relationship('Customer', back_populates='bookings')

    def __repr__(self):
        return f'Booking {self.id}, {self.booking_date}, {self.ticket.ticket_description}, {self.customer.customer_name}'
