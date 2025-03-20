
class A:
    
    def feature1(self):
        print('Feature 1 works') 
    
    def feature2(self):
        print('Feature 2 works') 

class B(A):
    
    def feature3(self):
        print('Feature 3 works') 
    
    def feature4(self):
        print('Feature 4 works') 

class D:
    def feature6(self):
        print('Feature 6 working')
        print('only if c does multiple inheritance this is printed by c')
class C(B, D):

    def feature5(self):
        print('Feature 5 working')

features = B()

Cfeatures = C()

features.feature1()
features.feature2()
features.feature3()
features.feature4()

Cfeatures.feature6()