import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Employee:
    hra_percentage=20

    def __init__(self,emp_id,basic_salary):
        self.emp_id=emp_id
        self.basic_salary=basic_salary
        self.leave_days=0
        self.net_salary=0

    def calculate_salary(self):
        hra=self.basic_salary*Employee.hra_percentage/100
        self.net_salary=self.basic_salary+hra
        logging.info("Salary calculated for employee %s",self.emp_id)

    def apply_leave_deduction(self,days):
        if days<=0:
            logging.warning("Invalid leave days for employee %s",self.emp_id)
            return
        deduction=(self.basic_salary/30)*days
        self.net_salary=self.net_salary-deduction
        self.leave_days+=days
        logging.info("Leave deduction applied for employee %s",self.emp_id)

    def display_payslip(self):
        logging.info(
            "Payslip for %s Basic:%d HRA:%d%% LeaveDays:%d NetSalary:%d",
            self.emp_id,
            self.basic_salary,
            Employee.hra_percentage,
            self.leave_days,
            self.net_salary
        )

    @classmethod
    def update_hra_percentage(cls,percentage):
        if percentage<=0:
            logging.warning("Invalid HRA percentage entered")
            return
        cls.hra_percentage=percentage
        logging.info("HRA percentage updated to %d",percentage)


e1=Employee("EMP101",30000)
e1.calculate_salary()
e1.apply_leave_deduction(2)
e1.display_payslip()

Employee.update_hra_percentage(25)

e2=Employee("EMP102",40000)
e2.calculate_salary()
e2.display_payslip()
