
class Student:

    school = "All Saints Public School"

    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def getInfo():
        print("This is Student class of OOP module")

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
   
    
    def avg(self):
        return(self.m1 + self.m2 + self.m3)

std1 = Student(45, 40, 50)
std2 = Student(30, 35, 40)

print(f"Avg: {std1.avg()}")
print(f"Avg: {std2.avg()}")

print(Student.getSchool())

Student.getInfo()
