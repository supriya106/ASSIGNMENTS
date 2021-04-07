import weakref

class Student:
    _students = []
    def __init__(self,name,rollNo,age,gender):
        self.name = name
        self.rollNo = rollNo
        self.age = age
        self. gender = gender
        self.__class__._students.append(self)

        @classmethod
        def display(cls):
            for i in cls._students:
                print(i.name)

        @classmethod
        def delete(cls,std):
            cls._students.remove(std)
            print(std.name+"is removed from classroom")
            del std

        @classmethod
        def search(cls,rno):
            for i in cls._students:
                if i . rollNo==rno:
                    print("RollNo {} is {}".formate(rno,i.name))
                    break


            @classmethod
            def update(cls, rn,No):
                i = std1.search(rn)
                roll = No
                i.rollno = roll;

std1 = Student('riya',12,15,"female")
std2 = Student('Ram',10,14,"male")
Student.display()
Student.delete(std1)
Student.search(10)
Student.update()


