import logging

logging.basicConfig(
    filename="ecommerce.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Order:
    tax_percentage=5

    def __init__(self,order_id,quantity,price):
        self.order_id=order_id
        self.quantity=quantity
        self.price=price
        self.is_placed=False
        self.total_price=0

    def place_order(self):
        if self.quantity<=0 or self.price<=0:
            logging.warning("Invalid order details for %s",self.order_id)
            return
        if self.is_placed:
            logging.warning("Order already placed %s",self.order_id)
            return
        self.is_placed=True
        logging.info("Order placed %s",self.order_id)

    def cancel_order(self):
        if not self.is_placed:
            logging.warning("Cancel attempted without placing order %s",self.order_id)
            return
        self.is_placed=False
        self.total_price=0
        logging.info("Order cancelled %s",self.order_id)

    def calculate_total_price(self):
        if not self.is_placed:
            logging.warning("Price calculation attempted without order placement %s",self.order_id)
            return
        subtotal=self.quantity*self.price
        tax=subtotal*Order.tax_percentage/100
        self.total_price=subtotal+tax
        logging.info("Total price calculated for order %s",self.order_id)

    @classmethod
    def update_tax_percentage(cls,percentage):
        if percentage<=0:
            logging.warning("Invalid tax percentage entered")
            return
        cls.tax_percentage=percentage
        logging.info("Tax percentage updated to %d",percentage)


o1=Order("ORD301",2,1500)
o1.place_order()
o1.calculate_total_price()
o1.cancel_order()
o1.calculate_total_price()

Order.update_tax_percentage(10)

o2=Order("ORD302",1,2000)
o2.place_order()
o2.calculate_total_price()
