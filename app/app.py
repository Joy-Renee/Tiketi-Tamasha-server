from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import datetime
from models import db, Customer, Ticket, Booking, Event, Venue

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
CORS(app)

# with app.app_context():
#     db.create_all()


@app.route("/customers", methods=["GET", "POST"])
def customers():
    if request.method == "GET":
        customers = []
        for customer in Customer.query.all():
            customer_dict = customer.to_dict(rules=("-bookings",))
            customers.append(customer_dict)
        if len(customers) == 0:
            return jsonify({"Message": "There are no Customers"}), 404
        else:
            return make_response(jsonify(customers), 200)

    elif request.method == "POST":
        data = request.get_json()

        new_customer = Customer(
            customer_name=data.get("customer_name"),
            email=data.get("email"),
            phone_number=data.get("phone_number"),
            password=data.get("password"),
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"Message": "Customer was added successfuly"})


@app.route("/customer/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_customer(id):
    print(id)

    if request.method == "GET":
        customer = Customer.query.filter_by(id=id).first()
        if customer is None:
            return jsonify({"message": "Customer not found"}), 404

        one_customer = customer.to_dict(rules=("-bookings",))
        return jsonify(one_customer), 200

    elif request.method == "PUT":
        data = request.get_json()
        customer = Customer.query.get(id)

        if customer is None:
            return jsonify({"message": "Customer not found"}), 404

        if "customer_name" in data:
            customer.customer_name = data["customer_name"]
        if "email" in data:
            customer.email = data["email"]
        if "phone_number" in data:
            customer.phone_number = data["phone_number"]
        if "password" in data:
            customer.password = data["password"]

        db.session.commit()

        return jsonify({"message": "Customer details updated successfully"}), 200

    elif request.method == "DELETE":
        customer = Customer.query.filter_by(id=id).first()
        if customer is None:
            return jsonify({"message": "Customer not found"}), 404

        Booking.query.filter_by(customer_id=customer.id).delete()

        db.session.delete(customer)
        db.session.commit()

        return jsonify({"message": "Customer deleted successfully"}), 200


@app.route("/bookings", methods=["GET", "POST"])
def bookings():
    if request.method == "GET":
        bookings = []
        for book in Booking.query.all():
            book_dict = book.to_dict(rules=("-ticket", "-customer"))
            bookings.append(book_dict)
        if len(bookings) == 0:
            return jsonify({"Message": "There are no bookings yet"}), 404
        else:
            return make_response(jsonify(bookings), 200)

    elif request.method == "POST":
        data = request.get_json()

        new_booking = Booking(
            booking_date=data.get("booking_date"),
            ticket_id=data.get("ticket_id"),
            customer_id=data.get("customer_id"),
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"Message": "Booking done successfuly"})


@app.route("/events", methods=["GET", "POST"])
def events():
    if request.method == "GET":
        events = []
        for event in Event.query.all():
            event_dict = event.to_dict()
            events.append(event_dict)
        if len(events) == 0:
            return jsonify({"Message": "There are no events yet"}), 404
        else:
            return make_response(jsonify(events), 200)
    elif request.method == "POST":
        data = request.get_json()
        new_event = Event(
            event_name=data.get("event_name"),
            event_date=data.get("event_date"),
            description=data.get("description"),
            event_time=data.get("event_time"),
            organizer_id=data.get("organizer_id"),
            venue_id=data.get("venue_id"),
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify({"Message": "Event created successfuly"})


@app.route("/event/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_event(id):

    if request.method == "GET":
        events = Event.query.filter(id == id).first()
        if events is None:
            return jsonify({"Message": "Event not found"}), 404
        event = events.to_dict()
        return jsonify(event), 200

    elif request.method == "DELETE":
        event = Event.query.filter(Event.id == id).first()
        if event is None:
            return jsonify({"Message": "Event not found"}), 404
        db.session.delete(event)
        db.session.commit()
        return jsonify({"Message": "Event deleted successfully"}), 200

    elif request.method == "PUT":
        event = Event.query.filter_by(id=id).first()
        if event is None:
            return jsonify({"Message": "Event not found"}), 404
        data = request.get_json()
        event.event_name = data.get("event_name", event.event_name)
        event.description = data.get("description", event.description)
        event.event_date = data.get("event_date", event.event_date)
        event.event_time = data.get("event_time", event.event_time)
        event.organizer_id = data.get("organizer_id", event.organizer_id)
        event.venue_id = data.get("venue_id", event.venue_id)
        db.session.commit()
        return jsonify(event.to_dict())


@app.route("/venues", methods=["GET", "POST"])
def venues():
    if request.method == "GET":
        venues = []
        for venue in Venue.query.all():
            venue_dict = venue.to_dict()
            venues.append(venue_dict)
            response = make_response(venues, 200)
            return response
    elif request.method == "POST":
        new_venue = Venue(
            name=request.form.get("name"),
            address=request.form.get("address"),
            capacity=request.form.get("capacity"),
        )
        db.session.add(new_venue)
        db.session.commit()
        venue_dict = new_venue.to_dict()
        response = make_response(venue_dict, 201)
        return response


@app.route("venues/<int:id>", method=["PATCH", "DELETE"])
def venue_by_id(id):
    if request.method == "DELETE":
        venue = Venue.query.filter(Venue.id == id).first()
        db.session.delete(venue)
        db.session.commit()
        response_body = {
            "Deleted successfuly": True,
            "message": "The venue has been successfully deleted",
        }
        response = make_response(response_body, 200)
        return response

    elif request.method == "PATCH":

        venue = Venue.query.filter(Venue.id == id).first()
        for attr in request.form:
            setattr(venue, attr, request.form.get(attr))
        db.session.add(venue)
        db.session.commit()
        venue_dict = venue.to_dict()
        response = make_response(venue_dict, 200)
        return response


@app.route("/tickets", methods=["GET", "POST"])
def tickets():
    if request.method == "GET":
        tickets = []
        for ticket in Ticket.query.all():
            ticket_dict = ticket.to_dict()
            tickets.append(ticket_dict)
            response = make_response(tickets, 200)
            return response
    elif request.method == "POST":
        new_ticket = Ticket(
            price=request.form.get("price"),
            ticket_type=request.form.get("ticket_type"),
            available=request.form.get("available"),
        )
        db.session.add(new_ticket)
        db.session.commit()
        ticket_dict = new_ticket.to_dict()
        response = make_response(ticket_dict, 201)
        return response


@app.route("tickets/<int:id>", method=["PATCH"])
def ticket_by_id(id):
    ticket = Ticket.query.filter(Ticket.id == id).first()
    for attr in request.form:
        setattr(ticket, attr, request.form.get(attr))
    db.session.add(ticket)
    db.session.commit()
    ticket_dict = ticket.to_dict()
    response = make_response(ticket_dict, 200)
    return response


if __name__ == "__main__":
    app.run(port=5555, debug=True)
