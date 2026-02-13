import logging

# Logging configuration
logging.basicConfig(
    filename="hostel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class HostelRoom:
    room_rent=5000   # class variable

    def __init__(self, room_no, student_name):
        self.room_no=room_no
        self.student_name=student_name
        self.is_allocated=False

    def allocate_room(self):
        if self.is_allocated:
            logging.warning("Room %s is already allocated", self.room_no)
            return

        self.is_allocated=True
        logging.info("Room %s allocated to %s", self.room_no, self.student_name)

    def vacate_room(self):
        if not self.is_allocated:
            logging.warning("Vacate attempted for unallocated room %s", self.room_no)
            return

        self.is_allocated=False
        logging.info("Room %s vacated by %s", self.room_no, self.student_name)

    def calculate_monthly_fee(self):
        if not self.is_allocated:
            logging.warning("Fee calculation attempted without allocation for room %s", self.room_no)
            return

        logging.info(
            "Monthly fee for room %s (student %s) is %d",
            self.room_no,
            self.student_name,
            HostelRoom.room_rent
        )
    @classmethod
    def update_room_rent(cls, rent):
        if rent<=0:
            logging.warning("Invalid room rent entered")
            return

        cls.room_rent=rent
        logging.info("Room rent updated to %d", rent)
h1 = HostelRoom("A101", "Akshaya")
h1.allocate_room()
h1.calculate_monthly_fee()
h1.vacate_room()
h1.calculate_monthly_fee()

HostelRoom.update_room_rent(6000)

h2 = HostelRoom("B202", "Sai")
h2.allocate_room()
h2.calculate_monthly_fee()

