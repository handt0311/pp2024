# Input number of students in a class
# • Input student information: id, name, DoB
# • Input number of courses
# • Input course information: id, name
# • Select a course, input marks for student in this course
def inp_nbstu():
    nb_stu = int(input("Input the number of students:"))
    return nb_stu
def inp_in4():
    students=[]
    nb_stu=inp_nbstu()
    for i in range(1,nb_stu+1):
        stu_id = input(f"Input the student ID {i}:")
        stu_name = input(f"Input the  name of student with ID {i}: ")
        stu_dob = input(f"Input the DOB of student with ID {i}: ")
        students.append({"ID":stu_id, "Name":stu_name, "DOB":stu_dob,"Marks":{}} )

    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, DOB: {student['DOB']}")

    return students
# inp_in4()

def inp_nbc():
    nb_c =  int(input("Input the number of courses:"))
    return nb_c
def inp_cin4():
    courses=[]
    nb_c = inp_nbc()
    for i in range(1,nb_c+1):
        c_id = input(f"Input the course ID {i}: ")
        c_name = input(f"Input the name of course with ID {i}:")
        courses.append({"ID":c_id, "Name":c_name})

    for course in courses:
        print(f"ID: {course['ID']}, Name: {course['Name']}")
    return courses
# inp_cin4()

def inp_marks(students, courses):
    c_id = input("Input the course ID you want to add marks:")
    if not any(course["ID"]==c_id for course in courses):# == thay bằng in cũng được
        print("Invalid course ID")
        return
    for student in students:
        mark= input(f"Input mark for student with ID {student['ID']}:")
        student["Marks"][c_id] = mark
        print(f"Mark for student with ID {student['ID']}: {mark}")

def list_c(courses):
    if len(courses) == 0:
        print("Chưa điền courses")
    else:
        for course in courses:
            print(f"Course {course['Name']} with ID {course['ID']}")

def list_stu(students):
    if len(students)  == 0:
        print("CHƯA CÓ HỌC SINH")
    else:
        for student in students:
            print(f"Student {student['Name']} with ID {student['ID']}")

def list_mark(students):
    c_id = input("Input the course ID you want to list:")
    if not any(c_id in student["Marks"] for student in students):
        print("Course ID không tồn tại")
    else:
        for student in students:
            print(f"Student {student['Name']} with ID {student['ID']} has mark {student['Marks'][c_id]} in course {c_id}")

# a=inp_in4()
# b=inp_cin4()
# inp_marks(a,b)
# list_mark(a)


def main():
    students=[]
    courses =[]
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
            inp_nbstu()
        elif options ==2:
            students = inp_in4()
        elif options == 3:
            inp_nbc()
        elif options == 4:
           course = inp_cin4()
        elif options == 5:
            students = inp_in4()
            courses = inp_cin4()
            if not students or not courses:
                print("Please input information for students and courses first")
            else:
                inp_marks(students,courses)
        elif options == 6: 
            list_stu(students) 
        elif options == 7:  
            list_c(courses)
        elif options == 8:
            list_mark(students)
if __name__ == "__main__":   
    main()