import logging

logging.basicConfig(
    filename="recharge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Recharge:
    validity_days = 28  

    def __init__(self, mobile_number, balance):
        self.mobile_number = mobile_number
        self.balance = balance
        self.validity = 0

    def do_recharge(self, amount):
        if amount <= 0:
            logging.warning("Invalid recharge amount entered")
            return
        self.balance += amount
        self.validity += Recharge.validity_days
        logging.info("Recharge of %d done for %s", amount, self.mobile_number)

    def check_validity(self):
        logging.info("Validity checked for %s and validity is %d", self.mobile_number,self.validity_days)

    def show_balance(self):
        logging.info("Balance checked for %s and balance is %d", self.mobile_number,self.balance)

    @classmethod
    def update_recharge_plans(cls, days):
        if days <= 0:
            logging.warning("Invalid validity days entered")
            return

        cls.validity_days = days
        logging.info("Recharge plan validity updated to %d days", days)
r1 = Recharge("9876543210", 50)
r1.show_balance()
r1.do_recharge(199)
r1.show_balance()
r1.check_validity()
Recharge.update_recharge_plans(56)
r2 = Recharge("9876543210", 20)
r2.do_recharge(299)
r2.show_balance()
r2.check_validity()

