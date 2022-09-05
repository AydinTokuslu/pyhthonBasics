class Person():
    def __init__(self, fname, lname) -> None:
        self.firstname=fname
        self.lastname=lname
        print('person created')
    def who_am_i(self):
        print('I am a personel')
    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number) -> None:
        Person.__init__(self, fname, lname)
        self.studentNumber=number
        print('student created')
        #override
    def who_am_i(self):
        print('I am a student')
    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch) -> None:
        super().__init__(fname, lname)
        self.branch=branch
    def who_am_i(self):
        print(f'I am a {self.branch} teacher') 


p1=Person('ali','yılmaz')
s1=Student('çınar','turan', 1256)
t1=Teacher('serkan','yılmaz','math')

print(p1.firstname+ ' '+ p1.lastname)
print(s1.firstname+ ' '+ s1.lastname+ ' '+ str(s1.studentNumber))

t1.who_am_i()
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()