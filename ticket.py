import logging

logging.basicConfig(
    filename="ticket.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Ticket:
    base_fare=500

    def __init__(self,ticket_id,seats):
        self.ticket_id=ticket_id
        self.seats=seats
        self.is_booked=False

    def book_ticket(self):
        if self.seats<=0:
            logging.warning("Invalid number of seats for booking")
            return
        if self.is_booked:
            logging.warning("Ticket already booked %s",self.ticket_id)
            return
        self.is_booked=True
        logging.info("Ticket %s booked with %d seat(s)",self.ticket_id,self.seats)

    def cancel_ticket(self):
        if not self.is_booked:
            logging.warning("Cancel attempted without booking %s",self.ticket_id)
            return
        self.is_booked=False
        logging.info("Ticket %s cancelled",self.ticket_id)

    def calculate_fare(self):
        if not self.is_booked:
            logging.warning("Fare calculation attempted without booking %s",self.ticket_id)
            return
        total=self.seats*Ticket.base_fare
        logging.info("Total fare for ticket %s is %d",self.ticket_id,total)

    @classmethod
    def update_base_fare(cls,fare):
        if fare<=0:
            logging.warning("Invalid base fare entered")
            return
        cls.base_fare=fare
        logging.info("Base fare updated to %d",fare)


t1=Ticket("RAIL101",2)
t1.book_ticket()
t1.calculate_fare()
t1.cancel_ticket()
t1.calculate_fare()

Ticket.update_base_fare(700)

t2=Ticket("RAIL102",1)
t2.book_ticket()
t2.calculate_fare()
