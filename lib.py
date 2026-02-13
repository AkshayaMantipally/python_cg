import logging

logging.basicConfig(
    filename='library.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class LibraryBook:
    fine_per_day=5

    def __init__(self,book_id,title):
        self.book_id=book_id
        self.title=title
        self.is_issued=False
        self.is_returned=True
        self.days_late=0

    def issue_book(self):
        if self.is_issued and not self.is_returned:
            logging.warning("Book is already issued. Cannot issue again.")
        else:
            self.is_issued=True
            self.is_returned=False
            self.days_late=0
            logging.info("Book has been issued successfully.")

    def return_book(self, days_late):
        if not self.is_issued and self.is_returned:
            logging.warning("Book is already returned. Cannot return again.")
        else:
            self.is_issued=False
            self.is_returned=True
            self.days_late=days_late
            fine=self.calculate_fine()
            logging.info(f"Book returned successfully. Fine amount is fine")

    def calculate_fine(self):
        if self.days_late <= 0:
            return 0
        return self.days_late * LibraryBook.fine_per_day

    @classmethod
    def update_fine_per_day(cls, new_fine):
        if new_fine <= 0:
            logging.warning("Fine amount must be greater than zero.")
        else:
            cls.fine_per_day = new_fine
            logging.info(f"Fine per day has been updated to new_fine")

book = LibraryBook(101, "Python")
book.issue_book()
book.issue_book()
book.return_book(3)
book.return_book(1)
LibraryBook.update_fine_per_day(10)
