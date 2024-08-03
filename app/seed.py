from random import randint
from faker import Faker

from app import app
from models import db, Customer, Ticket, Booking

with app.app_context():

    fake = Faker()

    Customer.query.delete()
    # Event.query.delete()
    Ticket.query.delete()
    # Venue.query.delete()
    Booking.query.delete()

    customers = []
    # events = []
    tickets = []
    # venues = []
    bookings = []

    for n in range(10):
        customer = Customer(customer_name=fake.first_name(), email = fake.email(), phone_number=fake.phone_number(), password = fake.password())
        customers.append(customer)

        # event = Event(event_name=fake.name(), ticket_description = fake.name(), event_date =fake.date(), event_time=fake.time())
        # events.append(event)

        rand_ticket = randint(1,10)
        ticket = Ticket(ticket_description=fake.name(), ticket_price=fake.numerify(), ticket_type=fake.name(), available=fake.numerify())
        tickets.append(ticket)

        # venue = Venue(venue_name=fake.name(), address =fake.address(), capacity=fake.numerify())
        # venues.append(venue)
        
        rand_booking = randint(1,10)
        rand_cust = randint(1,10)
        booking =  Booking(booking_date=fake.date(), ticket_id=rand_booking, customer_id=rand_cust)
        bookings.append(booking)

    
    db.session.add_all(customers)
    # db.session.add_all(events)
    db.session.add_all(tickets)
    # db.session.add_all(venues)
    db.session.add_all(bookings)


    db.session.commit()