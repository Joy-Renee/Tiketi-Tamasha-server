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
    phone_number = db.Column(db.String, nullable=False)
    password = db.Column(db.String)

    bookings = db.relationship('Booking', back_populates='customer', cascade='all, delete-orphan')
    orders = db.relationship('Order', back_populates='customer', cascade='all, delete-orphan')

    serialize_rules = ("-bookings.customer", "-order.customer")

    def __repr__(self):
        return f'<Customer {self.id}, {self.customer_name}, {self.email}, {self.phone_number}, {self.password}>'


class Ticket(db.Model, SerializerMixin):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    ticket_description = db.Column(db.String)
    ticket_price = db.Column(db.Integer)
    ticket_type = db.Column(db.String)
    available = db.Column(db.Integer)

    bookings = db.relationship('Booking', back_populates='ticket', cascade='all, delete-orphan')

    serialize_rules = ("-bookings.ticket",)

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

    serialize_rules = ("-ticket.bookings", "-customer.bookings",)

    def __repr__(self):
        return f'Booking {self.id}, {self.booking_date}, {self.ticket.ticket_description}, {self.customer.customer_name}'


class Organizer(db.Model, SerializerMixin):
    __tablename__ = 'organizers'

    id = db.Column(db.Integer, primary_key=True)
    organizer_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    password = db.Column(db.String(60))
    
    events = db.relationship('Event', back_populates='organizer', cascade='all, delete-orphan')

    serialize_rules = ("-events.organizer",)

    def __repr__(self):
        return f'<Organizer {self.id}, {self.organizer_name}, {self.email}, {self.phone_number}, {self.password}>'


class Venue(db.Model, SerializerMixin):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    capacity = db.Column(db.Integer)
    
    events = db.relationship('Event', back_populates='venue', cascade='all, delete-orphan')

    serialize_rules = ("-events.venue",)

    def __repr__(self):
        return f'<Venue {self.id}, {self.name}, {self.address}, {self.capacity}>'


class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String)
    description = db.Column(db.String)
    event_date = db.Column(db.String)
    event_time = db.Column(db.String)
    organizer_id = db.Column(db.Integer, db.ForeignKey('organizers.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    
    organizer = db.relationship('Organizer', back_populates='events')
    venue = db.relationship('Venue', back_populates='events')

    serialize_rules = ("-organizer.events", "-venue.events",)

    def __repr__(self):
        return f"<Event {self.event_name}', '{self.event_date}>"

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    order_date = db.Column(db.DateTime)
    total_price = db.Column(db.Float)

    customer = db.relationship('Customer', back_populates='orders')
    payment = db.relationship('Payment', back_populates='orders')

    serialize_rules = ("-customer.orders", "-payment.orders",)
    def __repr__(self):
        return f'<Order {self.id}, {self.customer_id}, {self.order_date}, {self.order_total}>'

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    payment_date = db.Column(db.DateTime)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

    orders = db.relationship('Order', back_populates='payment')

    serialize_rules = ("-orders.payment",)

    def __repr__(self):
        return f'<Payment {self.id}, {self.amount}, {self.payment_date}>'
