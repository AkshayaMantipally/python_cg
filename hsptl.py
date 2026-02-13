import logging

logging.basicConfig(
    filename='hsptl.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Patient:
    consult_fee = 200 

    def __init__(self, age, days):
        self.age = age
        self.days = days
        self.is_admitted = False

    def admit(self, status):
        if status:
            self.is_admitted = True
            logging.info("Patient admitted successfully")
        else:
            logging.warning("Invalid admission input")

    # Object method
    def discharge(self, status):
        if status and self.is_admitted:
            self.is_admitted = False
            logging.info("Patient discharged successfully")
        else:
            logging.warning("Patient is not admitted or invalid discharge input")

    # Object method
    def calculate_bill(self, disease):
        if not self.is_admitted or self.days <= 0:
            logging.warning("Billing failed: patient not admitted or invalid days")
            return

        if disease.lower() == "dengue":
            bill_amount = (self.days * 1000) + Patient.consult_fee
        else:
            bill_amount = (self.days * 2000) + Patient.consult_fee

        logging.info("Total bill amount: %d", bill_amount)

    @classmethod
    def update_consultation_fee(cls, new_fee):
        if new_fee <= 0:
            logging.warning("Invalid consultation fee")
        else:
            cls.consult_fee = new_fee
            logging.info("Consultation fee updated to %d", new_fee)

p1 = Patient(20, 5)
p1.admit(True)
p1.calculate_bill("dengue")
p1.discharge(True)
p2 = Patient(30, 3)
p2.calculate_bill("malaria")
p3 = Patient(25, 2)
p3.discharge(True)
p4 = Patient(40, 0)
p4.admit(True)
p4.calculate_bill("dengue")
Patient.update_consultation_fee(300)
Patient.update_consultation_fee(-100)
