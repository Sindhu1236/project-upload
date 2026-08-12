class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis(self):
        print("name",self.name)
        print("age",self.age)
class  student(person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def display(self):
        print("rollno", self.rollno)
s=student("abc",18,12)
s.dis()
s.display()

           