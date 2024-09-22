class Emp:
    ''' This is Doc String which tell us what class is for  '''

    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def empInfo(self):
        print('*'*10)
        print("emp no",self.eno)
        print("emp name",self.ename)
        print("emp sal ",self.esal)
        print("emp eaddr",self.eaddr)

print(Emp.__doc__)
e = Emp(101,'ashok',10000000,'Hyd')
e.empInfo()

e1 = Emp(102,'newashok',15000000,'hyd')
e1.empInfo()
