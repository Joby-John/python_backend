# DUCK TYPING
class PyCharm:

    def execute(self):
        print('Running PyCharm')
        print("Compiling")
        print('Running')

class MyEditor:

    def execute(self):
        print('\nRunning My Editor')
        print("Compiling")
        print('Running')
        print('Auto Correct')
        print('AI Assistant')
    
    
class Laptop:
    
    def code(self, ide):
        ide.execute()


lap1 = Laptop()

py1 = PyCharm()
my1 = MyEditor()

lap1.code(py1)
lap1.code(my1)


# OPERATOR OVERLOADING

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        total = Student(m1, m2)

        return total
    
    def __gt__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2

        if(m1>m2):
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
        
    
s1 = Student(78, 82)
s2 = Student(98, 100)

total = s1+s2

print(total.m1)
print(total.m2)

print("S1 Wins") if (s1>s2) else print("S2 Wins")
print(s1)
print(s2)

# Method overLoading 

class Sum:
    def __init__(self):
        pass

    def sum(self, a = None, b = None, c = None):

        if(a!=None and b != None and c != None):
            return a+b+c
        elif(a!=None and b!=None):
            return a+b
        else:
            return a


s1 = Sum()

print(s1.sum(1, 2, 3))

# Method Overriding

class A:

    
    def show(self):
        print('show in A')

class B(A):

    #This show overrides A's Show, that is, now B has show of its own so that show overrides A's
    def show(self):
        print('Show in B')

b = B()
b.show()
