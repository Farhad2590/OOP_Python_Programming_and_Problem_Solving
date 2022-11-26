class Student:
    def __init__(self,Name,id,age):
        self.Name = Name
        self.id = id
        self.age = age
class Course:
    def __init__(self,C_Name, C_Code, C_Teacher):
        self.C_Name = C_Name
        self.C_Code = C_Code
        self.C_Teacher = C_Teacher
class Teacher:
    def __init__(self,S_Name,S_Code) :
        self.S_Name = S_Name
        self.S_Code = S_Code