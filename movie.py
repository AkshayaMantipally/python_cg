import logging

logging.basicConfig(
    filename="movie.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class MovieTicket:
    ticket_price = 150

    def __init__(self, name, seats):
        self.name = name
        self.seats_booked = seats

    def book_seat(self):
        if self.seats_booked <= 0:
            logging.warning("User entered invalid number of seats for booking")
            return

        logging.info("%s booked %d seat(s)", self.name, self.seats_booked)


    def cancel_booking(self):
        if self.seats_booked <= 0:
            logging.warning("User tried to cancel without booking")
            return

        logging.info("%d seats cancelled successfully", self.seats_booked)
        self.seats_booked = 0

    def calculate_ticket_price(self):
        total = self.seats_booked * MovieTicket.ticket_price
        logging.info("%d total ticket price calculated for %s",total, self.name)

    @classmethod
    def update_ticket_price(cls, price):
        if price <= 0:
            logging.warning("Invalid ticket price entered for update")
            return

        cls.ticket_price = price
        logging.info("Ticket price updated to %d", price)


m1 = MovieTicket("MOV101", 3)
m1.book_seat()
m1.calculate_ticket_price()
m1.cancel_booking()
m1.calculate_ticket_price()

MovieTicket.update_ticket_price(200)

m2 = MovieTicket("MOV102", 2)
m2.book_seat()
m2.calculate_ticket_price()
