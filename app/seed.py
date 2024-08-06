from app import app
from models import db, Venue, Organizer, Event, Customer, Ticket, Booking, Payment, Order
from sqlalchemy.exc import IntegrityError
import datetime

def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Venue).delete()
        db.session.query(Organizer).delete()
        db.session.query(Event).delete()
        db.session.query(Customer).delete()
        db.session.query(Payment).delete()
        db.session.quer(Order).delete()
        db.session.query(Ticket).delete()
        db.session.query(Booking).delete()

        # Add Venues
        venues = [
            Venue(name="Uhuru Gardens", address="Langata Road", capacity=2000),
            Venue(name="Carnival Grounds", address="Mombasa", capacity=5000),
            Venue(name="Diani Resorts", address="Diani Mombasa", capacity=1500),
            Venue(name="KICC Grounds", address="Nairobi City Square", capacity=1000)
        ]
        db.session.add_all(venues)
        
        # Add Organizers
        organizers = [
            Organizer(organizer_name="James", email="james@example.com", phone_number=1234567890, password="password1"),
            Organizer(organizer_name="Victor", email="victor@example.com", phone_number=2345678901, password="password2"),
            Organizer(organizer_name="Joy", email="joy@example.com", phone_number=3456789012, password="password3")
        ]
        db.session.add_all(organizers)
        
        # Add Events
        events = [
            Event(
                event_name="Raha Fest",
                description="Meet the best international artist davido at raha fest and have a time of your life",
                venue=venues[0],
                event_date="2024-10-10",
                event_time="18:00",
                organizer=organizers[0]
            ),
            Event(
                event_name="Sol Fest",
                description="Party with akina sauti sol for a last juicy party",
                venue=venues[1],
                event_date="2024-11-12",
                event_time="19:00",
                organizer=organizers[1]
            ),
            Event(
                event_name="Summer Tides",
                description="Have the best summer of your life as you join us for summer tides for a great unforgettable party",
                venue=venues[2],
                event_date="2023-08-24",
                event_time="20:00",
                organizer=organizers[2]
            ),
            Event(
                event_name="Oktober Fest",
                description="Karibu OktobaFest, East Africa's biggest beer festival where we come together to celebrate our vibrant culture. Come see HOW WE DO all things culture in East Africa: From our food, music, dance, fashion, art, gaming & stories shared over beer that connects us to celebrate the culture we love.",
                venue=venues[2],
                event_date="2024-07-12",
                event_time="17:00",
                organizer=organizers[2]
            )
        ]
        db.session.add_all(events)
        
        # Add Customers
        customers = [
            Customer(customer_name="Kelvin", email="kelvin@example.com", phone_number=1234567890, password="password1"),
            Customer(customer_name="Mary", email="mary@example.com", phone_number=2345678901, password="password2"),
            Customer(customer_name="Maureen", email="maureen@example.co", phone_number=3456789012, password="password3")
        ]
        db.session.add_all(customers)
        
        # Add Tickets
        tickets = [
            Ticket(ticket_description="Regular", ticket_price=50.0, ticket_type="REG", available=100),
            Ticket(ticket_description="VIP", ticket_price=100.0, ticket_type="VIP", available=50),
            Ticket(ticket_description="Early Bird", ticket_price=30.0, ticket_type="EB", available=200)
        ]
        db.session.add_all(tickets)

        payments = [
            Payment(amount=50.0, payment_date=datetime.datetime.now()),
            Payment(amount=100.0, payment_date=datetime.datetime.now()),
            Payment(amount=30.0, payment_date=datetime.datetime.now())
        ]
        db.session.add_all(payments) 


        orders = [
            Order(customer=customers[0], order_date=datetime.datetime.now(), total_price= 200.0),
            Order(customer=customers[1], order_date=datetime.datetime.no(), total_price= 150.0),
            Order(customer=customers[2], order_date=datetime.datetime.now(), total_price= 300.0)
        ] 
        db.session.add_all(orders)

        

        # Add Bookings
        bookings = [
            Booking(booking_date=datetime.datetime.now(),ticket=tickets[0], customer=customers[0]),
            Booking(booking_date=datetime.datetime.now(),ticket=tickets[1], customer=customers[1]),
            Booking(booking_date=datetime.datetime.now(),ticket=tickets[2], customer=customers[2])
        ]
        db.session.add_all(bookings)

        # Commit the data to the database
        try:
            db.session.commit()
            print("Database seeded with new data!")
        except IntegrityError:
            db.session.rollback()
            print("Integrity error occurred. Database rollback.")

if __name__ == "__main__":
    seed_data()
