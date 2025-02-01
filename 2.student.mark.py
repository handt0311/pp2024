# Copy your practical work 1 to 2.student.mark.oop.py
# • Make it OOP’ed
# • Same functions
# • Proper attributes and methods
# • Proper encapsulation
# • Proper polymorphism
# • e.g. .input(), .list() methods

class Student:
    def __init__(self):
        self.__id =  input("Enter student id:")
        self.__name = input("Enter student name:")
        self.__dob = input("Enter student dob:")
        self.__marks = {}

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_mark(self,c_id):
        return self.__marks.get(c_id,None)
    def set_mark(self,c_id,mark):
        self.__marks[c_id]= mark
   
    

class Courses:
    def __init__(self):
        self.__id = input("Enter course id:")
        self.__name = input("Enter course name:")
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id 
    
class Require:
    @staticmethod
    def input(args):
        return int(input(f"Enter the number of {args} : "))
    @staticmethod
    def list(sth):
        if not sth:
            print(f"You haven't entered {sth}")
        for i,sth in enumerate(sth):
            print(f"{i+1}. ID: {sth.get_id()}, name: {sth.get_name()}")
    
class University:
    def __init__(self):
        self.__nbstu = 0
        self.__nbc = 0
        self.__students = []
        self.__courses = []
    def get_nbstu(self):
        return self.__nbstu
    def get_nbc(self):
        return self.__nbc
    def get_students(self):
        return self.__students
    def get_courses(self):
        return self.__courses
    
    def set_nbstu(self):
        self.__nbstu = Require.input("students")
    
    def set_nbc(self):
        self.__nbc = Require.input("courses")

    def set_students(self):
        for i in range(self.__nbstu):
            self.__students.append(Student())

    def set_courses(self):
        for i in range(self.__nbc):
            self.__courses.append(Courses())
    def list_students(self):
        Require.list(self.__students)
    
    def list_courses(self):
        Require.list(self.__courses)
    def inp_marks(self):
        c_id = input("Input the course ID you want to add marks:")
        if not any(cou.get_id() == c_id for cou in self.__courses):# == thay bằng in cũng được
            print("Invalid course ID")
        else:
            for stu in self.__students:
                mark= input(f"Input mark for student with ID {stu.get_id()}:")
                stu.set_mark(c_id,mark)
    def list_marks(self):
        course_id = input("Enter the course ID you want to show: ")
        if not any(course_id in a.get_id() for a in self.__courses):
            print("Invalid course ID.")
        else:
            for student in self.__students:
                mark =student.get_mark(course_id)
                print(f" ID: {student.get_id()}, Name: {student.get_name()}, Mark: {mark}")

        
def main():
    univ = University()
    while True:
        print("""Choose the following options:
              0. Exist sign
              1. Input number of students
              2. Input student information
              3. Input number of courses
              4. Input course information
              5. Input marks for students in courses
              6. List students
              7. List courses
              8. List marks""")
        options = int(input("Enter your options:"))
        if options == 0:
            print("Existed")
            break
        elif options == 1:
            univ.set_nbstu()
        elif options ==2:
            univ.set_students()
        elif options == 3:
            univ.set_nbc()
        elif options == 4:
           univ.set_courses()
        elif options == 5:
            univ.set_nbstu()
            univ.set_nbc()
            univ.set_students()
            univ.set_courses()
            univ.inp_marks()

        elif options == 6: 
            univ.list_students()
        elif options == 7:  
            univ.list_courses()
        elif options == 8:
            univ.list_marks()
if __name__ == "__main__":   
    main()