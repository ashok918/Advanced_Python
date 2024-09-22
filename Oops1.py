class Student:
    '''
    This class developer by Ashok demo purpose
    This is Know as doc string
    '''
    def __init__(self,rollno,name):
        self.name = name
        self.rollno = rollno

    def talk(self):
        print(f"Hello my name is ",self.name)
        print("hello my roll num", self.rollno)

print(Student.__doc__)
help(Student)
s1 = Student('ashok',101)
print(s1.name)
print(s1.rollno)
s1.talk()

s2 = Student('kumar',102)
print(s2.name)
print(s2.rollno)
s2.talk()


