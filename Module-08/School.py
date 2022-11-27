class Student:
    def __init__(self,Name,id,age):
        self.Name = Name
        self.age = age
        self.id = id
class Course:
    def __init__(self,C_Name, C_Code, C_Teacher):
        self.C_Name = C_Name
        self.C_Code = C_Code
        self.C_Teacher = C_Teacher
class Teacher:
    def __init__(self,S_Name,S_Code) :
        self.S_Name = S_Name
        self.S_Code = S_Code

class School:
    def __init__(self, S_Name,Courses,Teachers,Students):
        self.Name = S_Name
        self.Courses = Courses
        self.Teachers = Teachers
        self.Students = Students

    def Get_students_Info(self):
        for Student in self.Students:
            print(Student.Name, Student.age, Student.id)

school_name = 'Phitron'

Algo_Course = Course('Sowmitro Das','CSE331', 'Algorithm')
Teacher1 = Teacher('Sowmitro Das',Algo_Course )
DS_Course = Course('Morshed Rana','CSE332', 'Data Structure')
Teacher4 = Teacher('Morshed Rana',DS_Course )
Pattern_Course = Course('Jahid Hasan','CSE333', 'Pattern Recognition')
Teacher3 = Teacher('Jahid Hasan',Pattern_Course )
TOC_Course = Course('Shafayet Nur','CSE334', 'Theory Of Computing')
Teacher2 = Teacher('Shafayet Nur',TOC_Course )
OOP_Course = Course('Meherab Hosen','CSE335', 'Object Oriented Programming')
Teacher5 = Teacher('Meherab Hosen',OOP_Course )

Student1 = Student('Farhad Hossen', 21, 'CSE02006954')
Student2 = Student('Nafisa Lubaba', 20, 'CSE02006930')
Student3 = Student('Shahriar Islam', 22, 'CSE02006936')
Student4 = Student('Saifa Tasnim', 20, 'CSE02006919')
Student5 = Student('Taspiya Alam', 20, 'CSE02006913')
Student6 = Student('Saidul Islam', 24, 'CSE02006908')
Student7 = Student('Sadia Humaira', 22, 'CSE02006904')
Student8 = Student('Shimanta Barua', 23, 'CSE02006905')
Student9 = Student('Sakib Rayhan Nahid', 24, 'CSE02006906')
Student10 = Student('Aminul Islam', 22, 'CSE02006910')

Teachers = [Teacher1,Teacher2,Teacher3,Teacher4,Teacher5]

Courses = [OOP_Course,TOC_Course,Pattern_Course,DS_Course,Algo_Course]

Students = [Student1,Student2,Student3,Student4,Student5,Student6,Student7,Student8,Student9,Student10]

My_School = School( school_name,Teachers,Courses,Students)
# print(My_School.Students)
My_School.Get_students_Info()
