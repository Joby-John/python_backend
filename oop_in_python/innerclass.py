
class Student:

    def __init__(self, name, rollNo):
        self.name = name
        self.roll = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Joby', 34)

s1.show()


lap1 = Student.Laptop()