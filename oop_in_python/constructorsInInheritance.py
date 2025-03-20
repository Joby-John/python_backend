
class A:
    def __init__(self):
        print('Init of A class')
    
    def feature1(self):
        print('Feature 1 works') 
    
class B:

    #A's init is only called if theres no init for B
    def __init__(self):
        #Super can be used to access method of A
        super().__init__()
        print('Init of B')
    
    def feature2(self):
        print('Feature 2 works') 

class C(A, B):

    def __init__(self):
        super().__init__()
        print('in C init')
    
    def feature3(self):
        super().feature2()


c = C()

c.feature3()


