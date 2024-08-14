from app import app
from models import db, Venue, Organizer, Event, Customer, Ticket, Booking, Payment, Order
from sqlalchemy.exc import IntegrityError
import datetime

def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Booking).delete()
        db.session.query(Ticket).delete()
        db.session.query(Payment).delete()
        db.session.query(Order).delete()
        db.session.query(Event).delete()
        db.session.query(Venue).delete()
        db.session.query(Organizer).delete()
        db.session.query(Customer).delete()
        db.session.commit()

        # Add Venues
        venues = [
            Venue(name="Uhuru Gardens", address="Langata Road", capacity=9000, image="https://lh3.googleusercontent.com/P6kpuuIYXzr5ERF1-76XjHhdvbm6e-WUcTFJt94ppSQVVtvySQ3JVV6bGj5RjT4atrYEIlQVpHeerV9OS5CBOGwa_YwWna2hznTv7A=s750", venue_price=5000.00),
            Venue(name="Carnival Grounds", address="Mombasa", capacity=5000, image="https://www.shutterstock.com/image-photo/nairobi-kenya-september-15-2013-260nw-771906451.jpg", venue_price=5000.00),
            Venue(name="Diani Resorts", address="Diani Mombasa", capacity=1500, image ="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/56/73/ed/diani-sea-resort.jpg?w=700&h=-1&s=1", venue_price=5000.00),
            Venue(name="KICC Grounds", address="Nairobi City Square", capacity=1000, image="https://ocdn.eu/images/pulscms/MWM7MDA_/0e3817b9f5dd05c254990d47eb0c685f.jpeg", venue_price=5000.00),
            Venue(name="Quiver Kilimani", address="Ngong Road prestige", capacity=1500, image="https://i.ytimg.com/vi/4meykCSeckg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCnUmJwqhA-fuiDMCRilttlSPSaLw", venue_price=5000.00),
            Venue(name="Emara Ole Sereni", address="Nairobi next to Nairobi nattional park", capacity=500, image="https://cf.bstatic.com/xdata/images/hotel/max1024x768/484982054.jpg?k=a30ad26e24899dbd982b7dc6613ab68a0508acf6b1fcaba497b90a868d14f0ec&o=&hp=1", venue_price=5000.00),
            Venue(name="Tamasha Eldoret", address="Eldoret", capacity=2000, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnXQ81ZAJ4Di8K-itdoakn-vY7RCmFweyQ5w&s", venue_price=5000.00),
            Venue(name="Jamii Executive Gardens", address="mwea", capacity=3000, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOKQgbwKQ85CArXWaAd5Fb1WO01deTbwPmT2olAtwFtzr--9GVeIEv17674gMKWNyofu4&usqp=CAU", venue_price=5000.00),
            Venue(name="Ngong Racecourse", address="Ngong", capacity=1000, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9BSZomf8Ks5R4ddnHEGjCpcjyYuVRKyPWYQ&s", venue_price=5000.00),
            Venue(name="Hells gate national park", address="Naivasha", capacity=8000, image="https://cdn.standardmedia.co.ke/images/sunday/wzmkpihitqrstob5d6bf41808241.jpg", venue_price=5000.00),
            Venue(name="K1 lounge", address="Westlands", capacity=1500, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlAg3ONmytH1crE5DX7t2KuSooErOSCnnD6A&s", venue_price=5000.00),
            Venue(name="The Embassy", address="thika road roasters", capacity=1000, image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3jV1yZ_6oPYGINnBKA4hGSY7LsWTMB_RTjw&s", venue_price=5000.00),
        ]
        db.session.add_all(venues)
        
        # Add Organizers
        organizers = [
            Organizer(organizer_name="James", email="james@example.com", phone_number=1234567890, password="password1"),
            Organizer(organizer_name="Victor", email="victor@example.com", phone_number=2345678901, password="password2"),
            Organizer(organizer_name="Joy", email="joy@example.com", phone_number=3456789012, password="password3"),
            Organizer(organizer_name="kelnie", email="kelnie@example.com", phone_number=112343444, password="password4"),
            Organizer(organizer_name="julie", email="julie@example.com", phone_number=34535666432, password="password5")
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
                organizer=organizers[0],
                image="https://pbs.twimg.com/profile_images/1742193233956843520/zG4HrUJG_400x400.jpg"
            ),
            Event(
                event_name="Sol Fest",
                description="Party with akina sauti sol for a last juicy party",
                venue=venues[1],
                event_date="2024-11-12",
                event_time="19:00",
                organizer=organizers[1],
                image="https://citizentv.obs.af-south-1.myhuaweicloud.com/71068/conversions/Sol-Fest-og_image.webp"
            ),
            Event(
                event_name="Summer Tides",
                description="Have the best summer of your life as you join us for summer tides for a great unforgettable party",
                venue=venues[2],
                event_date="2023-08-24",
                event_time="20:00",
                organizer=organizers[2],
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeGMSLbcHEJFGuWvxiQrdHOQ4hLopBKSwcnw&s"
            ),
            Event(
                event_name="Oktober Fest",
                description="Karibu OktobaFest, East Africa's biggest beer festival where we come together to celebrate our vibrant culture. Come see HOW WE DO all things culture in East Africa: From our food, music, dance, fashion, art, gaming & stories shared over beer that connects us to celebrate the culture we love.",
                venue=venues[1],
                event_date="2024-07-12",
                event_time="17:00",
                organizer=organizers[2],
                image="https://nnmedia.nation.africa/uploads/2022/11/DNOktoberfest3010bta.jpg"
            ),
            Event(
                event_name="Raha Rava",
                description="Join us for the best party of the year at raha rava with the bahatis and one on one with ruger",
                venue=venues[11],
                event_date="2024-08-12",
                event_time="20:00",
                organizer=organizers[4],
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzShbFMvCzqPRDLZ69MOkFgBFvkQB-gGTf_g&s"
            ),
            Event(
                event_name="Color Festival",
                description="Experience the vibrant fusion of music, art, and pure joy at Nairobi Colour Festival on April 20th! Join us for an unforgettable celebration! ",
                venue=venues[1],
                event_date="2024-04-20",
                event_time="18:00",
                organizer=organizers[3],
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ2tzn_VsnbOqvhpWQgf9UVrtEJFEmeFVjdQ&s"
            ),
            Event(
                event_name="WRC VASHA",
                description="Held on the untamed terrains of Africas breathtaking landscapes where the weather can change in a matter of minutes. Mud, rocks fesh-fesh sand and challenging water crossings make safari rally kenya the ultimate test of enduarance",
                venue=venues[9],
                event_date="2024-03-12",
                event_time="08:00",
                organizer=organizers[3],
                image="https://www.president.go.ke/wp-content/uploads/1-195-scaled.jpeg"
            ),
            Event(
                event_name="juice party",
                description="The Eldoret Jyuuce Party is happening on 15 June! Grab your early bird tickets ASAP! All details are on the poster",
                venue=venues[6],
                event_date="2024-06-15",
                event_time="19:00",
                organizer=organizers[2],
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVVQSotjssyWmwGMmitFoSD6CLLPYwa0INEg&s"
            ),
            Event(
                event_name="Afrika moja",
                description="Concert is happening on 30th April @ KICC Grounds from 6PM, featuring Harmonize “Konde Boy” from Tanzania & other leading Kenyan artists. Eric Omondi & Iddi Achieng will be the MCs",
                venue=venues[3],
                event_date="2024-04-30",
                event_time="21:00",
                organizer=organizers[3],
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6OMO8pAIW-wMBaI9wsc0mEISutG92TydDGg&s"
            ),
            Event(
                event_name="New Years eve party",
                description="NEW YEAR'S EVE ALERT!🔥The climax party of the year will be @k1klubhouse with Kay Wachira Wanja & Gibbz Tha Daqchild Countdown to 2025 with fireworks!!💥",
                venue=venues[10],
                event_date="2024-12-31",
                event_time="22:00",
                organizer=organizers[4],
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-ormLjBoELRcfY9_ltWxAYDlJonvd_90YJw&s"
            ),
            Event(
                event_name="Roof Top Bash",
                description="Join us for a night of fun and games at the Roof Top Bash on 25 october at ole serei roof top",
                venue=venues[5],
                event_date="2024-10-25",
                event_time="17:00",
                organizer=organizers[3],
                image="https://emara.ole-sereni.com/wp-content/uploads/2022/11/s5.jpg"
            ),
            Event(
                event_name="Walker town",
                description="At Walker Town, consumers experience the best brand experience, entertainment (international artists, DJs and Acts), the best food, activities such as gaming, fashion and art, a truly in-culture space to take envious selfies and most importantly sample and experience the best Johnnie Walker drink creations by world-class mixologists, Whisky food pairings and much more",
                venue=venues[0],
                event_date="2024-03-18",
                event_time="18:00",
                organizer=organizers[1],
                image="https://i.ytimg.com/vi/AzCbrMo5598/maxresdefault.jpg"
            )
        ]
        db.session.add_all(events)
        
        # Add Customers
        customers = [
            Customer(customer_name="Kelvin", email="kelvin@example.com", phone_number=1234567890, password="password1"),
            Customer(customer_name="Mary", email="mary@example.com", phone_number=2345678901, password="password2"),
            Customer(customer_name="Maureen", email="maureen@example.com", phone_number=3456789012, password="password3")
        ]
        db.session.add_all(customers)
        
        # Add Tickets
        tickets = [
            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=500, event=events[0]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=1500, event=events[0]),
            Ticket(ticket_description="Vip", ticket_price=200.0, ticket_type="VIP", available=1200, event=events[0]),

            Ticket(ticket_description="Early Bird", ticket_price=100.0, ticket_type="EB", available=2000, event=events[1]),
            Ticket(ticket_description="Regular", ticket_price=150.0, ticket_type="REG", available=2000, event=events[1]),
            Ticket(ticket_description="Vip", ticket_price=250.0, ticket_type="VIP", available=1000, event=events[1]),

            Ticket(ticket_description="Early Bird", ticket_price=80.0, ticket_type="EB", available=300, event=events[2]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=700, event=events[2]),
            Ticket(ticket_description="Vip", ticket_price=250.0, ticket_type="VIP", available=500, event=events[2]),

            Ticket(ticket_description="Early Bird", ticket_price=110.0, ticket_type="EB", available=1000, event=events[3]),
            Ticket(ticket_description="Regular", ticket_price=250.0, ticket_type="REG", available=2500, event=events[3]),
            Ticket(ticket_description="Vip", ticket_price=300.0, ticket_type="VIP", available=1500, event=events[3]),

            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=500, event=events[4]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=1500, event=events[4]),
            Ticket(ticket_description="Vip", ticket_price=200.0, ticket_type="VIP", available=1200, event=events[4]),

            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=200, event=events[5]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=500, event=events[5]),
            Ticket(ticket_description="Vip", ticket_price=200.0, ticket_type="VIP", available=300, event=events[5]),

            Ticket(ticket_description="Early Bird", ticket_price=70.0, ticket_type="EB", available=2200, event=events[6]),
            Ticket(ticket_description="Regular", ticket_price=140.0, ticket_type="REG", available=3800, event=events[6]),
            Ticket(ticket_description="Vip", ticket_price=280.0, ticket_type="VIP", available=2000, event=events[6]),

            Ticket(ticket_description="Early Bird", ticket_price=25.0, ticket_type="EB", available=1000, event=events[7]),
            Ticket(ticket_description="Regular", ticket_price=45.0, ticket_type="REG", available=500, event=events[7]),
            Ticket(ticket_description="Vip", ticket_price=70.0, ticket_type="VIP", available=500, event=events[7]),

            Ticket(ticket_description="Early Bird", ticket_price=30.0, ticket_type="EB", available=100, event=events[8]),
            Ticket(ticket_description="Regular", ticket_price=70.0, ticket_type="REG", available=450, event=events[8]),
            Ticket(ticket_description="Vip", ticket_price=90.0, ticket_type="VIP", available=450, event=events[8]),

            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=200, event=events[9]),
            Ticket(ticket_description="Regular", ticket_price=70.0, ticket_type="REG", available=650, event=events[9]),
            Ticket(ticket_description="Vip", ticket_price=100.0, ticket_type="VIP", available=650, event=events[9]),

            Ticket(ticket_description="Early Bird", ticket_price=20.0, ticket_type="EB", available=50, event=events[10]),
            Ticket(ticket_description="Regular", ticket_price=50.0, ticket_type="REG", available=250, event=events[10]),
            Ticket(ticket_description="Vip", ticket_price=90.0, ticket_type="VIP", available=150, event=events[10]),

            Ticket(ticket_description="Early Bird", ticket_price=60.0, ticket_type="EB", available=3000, event=events[11]),
            Ticket(ticket_description="Regular", ticket_price=80.0, ticket_type="REG", available=3000, event=events[11]),
            Ticket(ticket_description="Vip", ticket_price=120.0, ticket_type="VIP", available=3000, event=events[11]),

            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=500, event=events[0]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=1500, event=events[0]),
            Ticket(ticket_description="Vip", ticket_price=200.0, ticket_type="VIP", available=1200, event=events[0]),

            Ticket(ticket_description="Early Bird", ticket_price=100.0, ticket_type="EB", available=2000, event=events[1]),
            Ticket(ticket_description="Regular", ticket_price=150.0, ticket_type="REG", available=2000, event=events[1]),
            Ticket(ticket_description="Vip", ticket_price=250.0, ticket_type="VIP", available=1000, event=events[1]),

            Ticket(ticket_description="Early Bird", ticket_price=80.0, ticket_type="EB", available=300, event=events[2]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=700, event=events[2]),
            Ticket(ticket_description="Vip", ticket_price=250.0, ticket_type="VIP", available=500, event=events[2]),

            Ticket(ticket_description="Early Bird", ticket_price=110.0, ticket_type="EB", available=1000, event=events[3]),
            Ticket(ticket_description="Regular", ticket_price=250.0, ticket_type="REG", available=2500, event=events[3]),
            Ticket(ticket_description="Vip", ticket_price=300.0, ticket_type="VIP", available=1500, event=events[3]),

            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=500, event=events[4]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=1500, event=events[4]),
            Ticket(ticket_description="Vip", ticket_price=200.0, ticket_type="VIP", available=1200, event=events[4]),

            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=200, event=events[5]),
            Ticket(ticket_description="Regular", ticket_price=100.0, ticket_type="REG", available=500, event=events[5]),
            Ticket(ticket_description="Vip", ticket_price=200.0, ticket_type="VIP", available=300, event=events[5]),

            Ticket(ticket_description="Early Bird", ticket_price=70.0, ticket_type="EB", available=2200, event=events[6]),
            Ticket(ticket_description="Regular", ticket_price=140.0, ticket_type="REG", available=3800, event=events[6]),
            Ticket(ticket_description="Vip", ticket_price=280.0, ticket_type="VIP", available=2000, event=events[6]),

            Ticket(ticket_description="Early Bird", ticket_price=25.0, ticket_type="EB", available=1000, event=events[7]),
            Ticket(ticket_description="Regular", ticket_price=45.0, ticket_type="REG", available=500, event=events[7]),
            Ticket(ticket_description="Vip", ticket_price=70.0, ticket_type="VIP", available=500, event=events[7]),

            Ticket(ticket_description="Early Bird", ticket_price=30.0, ticket_type="EB", available=100, event=events[8]),
            Ticket(ticket_description="Regular", ticket_price=70.0, ticket_type="REG", available=450, event=events[8]),
            Ticket(ticket_description="Vip", ticket_price=90.0, ticket_type="VIP", available=450, event=events[8]),

            Ticket(ticket_description="Early Bird", ticket_price=50.0, ticket_type="EB", available=200, event=events[9]),
            Ticket(ticket_description="Regular", ticket_price=70.0, ticket_type="REG", available=650, event=events[9]),
            Ticket(ticket_description="Vip", ticket_price=100.0, ticket_type="VIP", available=650, event=events[9]),

            Ticket(ticket_description="Early Bird", ticket_price=20.0, ticket_type="EB", available=50, event=events[10]),
            Ticket(ticket_description="Regular", ticket_price=50.0, ticket_type="REG", available=250, event=events[10]),
            Ticket(ticket_description="Vip", ticket_price=90.0, ticket_type="VIP", available=150, event=events[10]),

            Ticket(ticket_description="Early Bird", ticket_price=60.0, ticket_type="EB", available=3000, event=events[11]),
            Ticket(ticket_description="Regular", ticket_price=80.0, ticket_type="REG", available=3000, event=events[11]),
            Ticket(ticket_description="Vip", ticket_price=120.0, ticket_type="VIP", available=3000, event=events[11]),

        ]
        db.session.add_all(tickets)

        # Add Orders
        orders = [
            Order(customer=customers[0], order_date=datetime.datetime.now(), total_price=200.0),
            Order(customer=customers[1], order_date=datetime.datetime.now(), total_price=150.0),
            Order(customer=customers[2], order_date=datetime.datetime.now(), total_price=300.0)
        ]
        db.session.add_all(orders)

        # Add Payments
        payments = [
            Payment(amount=50.0, payment_date=datetime.datetime.now(), orders=orders[0]),
            Payment(amount=100.0, payment_date=datetime.datetime.now(), orders=orders[1]),
            Payment(amount=30.0, payment_date=datetime.datetime.now(), orders=orders[2])
        ]
        db.session.add_all(payments)
        
        # payments = [
        #     Payment(amount=50.0, payment_date=datetime.datetime.now(), orders=orders[0]),
        #     Payment(amount=100.0, payment_date=datetime.datetime.now(), orders=orders[1]),
        #     Payment(amount=30.0, payment_date=datetime.datetime.now(), orders=orders[2])
        # ]
        # db.session.add_all(payments)


        # orders = [
        #     Order(customer=customers[0], order_date=datetime.datetime.now(), total_price= 200.0),
        #     Order(customer=customers[1], order_date=datetime.datetime.now(), total_price= 150.0),
        #     Order(customer=customers[2], order_date=datetime.datetime.now(), total_price= 300.0)
        # ] 
        # db.session.add_all(orders)

        

        # Add Bookings
        bookings = [
            Booking(booking_date=datetime.datetime.now(), ticket=tickets[0], customer=customers[0]),
            Booking(booking_date=datetime.datetime.now(), ticket=tickets[1], customer=customers[1]),
            Booking(booking_date=datetime.datetime.now(), ticket=tickets[2], customer=customers[2])
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
