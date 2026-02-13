import logging

logging.basicConfig(
    filename='exam.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Exam:
    pass_marks = 40

    def __init__(self, student_name, total_marks, obtained_marks=0):
        self.student_name = student_name
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks
        self.is_started = False
        self.is_submitted = False

    def start_exam(self):
        if not self.is_started:
            self.is_started = True
            logging.info("Exam started for %s", self.student_name)
        else:
            logging.warning("Exam already started")

    def submit_exam(self):
        if self.is_started and not self.is_submitted:
            self.is_submitted = True
            logging.info("Exam submitted by %s", self.student_name)
        else:
            logging.warning("Exam not started or already submitted")

    def calculate_score(self):
        if not self.is_submitted:
            logging.warning("Cannot calculate score as exam is not submitted")
            return

        percentage = (self.obtained_marks / self.total_marks) * 100

        if percentage >= Exam.pass_marks:
            logging.info("%s PASSED with %.2f%%", self.student_name, percentage)
        else:
            logging.info("%s FAILED with %.2f%%", self.student_name, percentage)

    @classmethod
    def update_pass_marks(cls, new_marks):
        if 0 < new_marks <= 100:
            cls.pass_marks = new_marks
            logging.info("Pass marks updated to %d%%", new_marks)
        else:
            logging.warning("Invalid pass marks")


e1 = Exam("Akshaya", 100, 75)
e1.start_exam()
e1.submit_exam()
e1.calculate_score()

e2 = Exam("aks", 100, 30)
e2.start_exam()
e2.calculate_score()

e3 = Exam("Anu", 100, 35)
e3.start_exam()
e3.submit_exam()
e3.calculate_score()

Exam.update_pass_marks(50)
