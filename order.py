import logging

logging.basicConfig(
    filename='order.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Order:
    tax_percentage = 5  

    def __init__(self, order_id, quantity, price_per_item):
        self.order_id = order_id
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.is_placed = False
        self.is_cancelled = False

    def place_order(self):
        if not self.is_placed:
            self.is_placed = True
            logging.info("Order %s placed successfully", self.order_id)
        else:
            logging.warning("Order already placed")

    def cancel_order(self):
        if self.is_placed and not self.is_cancelled:
            self.is_cancelled = True
            logging.info("Order %s cancelled", self.order_id)
        else:
            logging.warning("Order not placed or already cancelled")

    def calculate_total_price(self):
        if not self.is_placed or self.is_cancelled:
            logging.warning("Cannot calculate price: order inactive")
            return
        if self.quantity <= 0 or self.price_per_item <= 0:
            logging.warning("Invalid quantity or price")
            return
        base_price = self.quantity * self.price_per_item
        tax = (Order.tax_percentage / 100) * base_price
        total_price = base_price + tax
        logging.info("Total price for order %s is %.2f",self.order_id, total_price)

    @classmethod
    def update_tax_percentage(cls, new_tax):
        if new_tax < 0 or new_tax > 100:
            logging.warning("Invalid tax percentage")
        else:
            cls.tax_percentage = new_tax
            logging.info("Tax percentage updated to %d%%", new_tax)

o1 = Order("ORD201", 2, 1500)
o1.place_order()
o1.calculate_total_price()
o1.cancel_order()
o1.calculate_total_price()
Order.update_tax_percentage(10)
o2 = Order("ORD202", 1, 2000)
o2.place_order()
o2.calculate_total_price()
