
class Result10th:
    def __init__(self, name, phno, email, passyr10, clsname):
        self.name = name
        self.phno = phno
        self.email = email
        self.passyr10 = passyr10
        self.clsname = clsname

    def display_10th(self):
        print("10th Details")
        print("Name:", self.name)
        print("Phone:", self.phno)
        print("Email:", self.email)
        print("10th Pass Year:", self.passyr10)
        print("Class Name:", self.clsname)


class Result12th(Result10th):
    def __init__(self, name, phno, email, passyr10, clsname, passyr12, percentage12):
        super().__init__(name, phno, email, passyr10, clsname)
        self.passyr12 = passyr12
        self.percentage12 = percentage12

    def display_12th(self):
        print("12th Details")
        print("12th Pass Year:", self.passyr12)
        print("12th Percentage:", self.percentage12)


class ResultBE(Result12th):
    def __init__(self, name, phno, email, passyr10, clsname,
                 passyr12, percentage12, branch, university, percentagebe):
        super().__init__(name, phno, email, passyr10, clsname, passyr12, percentage12)
        self.branch = branch
        self.university = university
        self.percentagebe = percentagebe

    def display_all(self):
        print("Student Complete Academic Details")
        self.display_10th()
        self.display_12th()
        print("Details")
        print("Branch:", self.branch)
        print("University:", self.university)
        print("BE_Percentage:", self.percentagebe)


s1 = ResultBE(
    "Akshaya", 9876543210, "akshaya@gmail.com",2020, "10th-A",2022, 92.5,"CSE", "JNTUH", 85.4
)
s1.display_all()
