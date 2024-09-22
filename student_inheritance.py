class Person:               #Base Class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
        
class Student(Person):       #Sub Class
    def __init__(self,name,age,roll):
        Person.__init__(self,name,age)
        self.roll=roll
    def display_student(self):
        print("ROLL:",self.roll)

#Driver Code      
p=Person("ABC",34)
s1=Student("XYZ",19,101)
p.display()
s1.display()
s1.display_student()

#print(help(Student))
#print(isinstance(s1,Person))
#print(issubclass(Student, Person))