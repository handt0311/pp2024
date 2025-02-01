import curses
import numpy as np
import math

class Student:
    def __init__(self, stdscr):
        self.__id = self.get_input(stdscr, "Enter student ID:")
        self.__name = self.get_input(stdscr, "Enter student name:")
        self.__dob = self.get_input(stdscr, "Enter student DOB:")
        self.__marks = {}
        self.__gpa = 0
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def get_mark(self, c_id):
        return self.__marks.get(c_id, None)
    
    def set_mark(self, c_id, mark):
        self.__marks[c_id] = math.floor(mark * 10) / 10
    
    def get_gpa(self):
        return self.__gpa
    
    def calculate_gpa(self, courses):
        total_credit = 0
        weighted_sum = 0
        for course in courses:
            course_id = course.get_id()
            if course_id in self.__marks:
                weighted_sum += self.__marks[course_id] * course.get_credits()
                total_credit += course.get_credits()
        self.__gpa = weighted_sum / total_credit if total_credit > 0 else 0
    
    @staticmethod
    def get_input(stdscr, prompt):
        stdscr.addstr(prompt)
        stdscr.refresh()
        return stdscr.getstr().decode("utf-8")

class Course:
    def __init__(self, stdscr):
        self.__id = self.get_input(stdscr, "Enter course ID:")
        self.__name = self.get_input(stdscr, "Enter course name:")
        self.__credits = int(self.get_input(stdscr, "Enter course credits:"))
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
    @staticmethod
    def get_input(stdscr, prompt):
        stdscr.addstr(prompt)
        stdscr.refresh()
        return stdscr.getstr().decode("utf-8")

class University:
    def __init__(self, stdscr):
        self.__nbstu = 0
        self.__nbc = 0
        self.__students = []
        self.__courses = []
        self.stdscr = stdscr
    
    def set_nbstu(self):
        self.stdscr.addstr("Enter number of students: ")
        curses.echo()
        self.__nbstu = int(self.stdscr.getstr().decode("utf-8"))
        curses.noecho()
    
    def set_nbc(self):
        self.stdscr.addstr("Enter number of courses: ")
        curses.echo()
        self.__nbc = int(self.stdscr.getstr().decode("utf-8"))
        curses.noecho()
    def add_student(self):
        if len(self.__students) < self.__nbstu:
            self.__students.append(Student(self.stdscr))
        else:
            self.stdscr.addstr("Maximum number of students reached!\n")
            self.stdscr.refresh()
            self.stdscr.getch()
    
    def add_course(self):
        if len(self.__courses) < self.__nbc:
            self.__courses.append(Course(self.stdscr))
        else:
            self.stdscr.addstr("Maximum number of courses reached!\n")
            self.stdscr.refresh()
            self.stdscr.getch()
    
    def input_marks(self):
        self.stdscr.addstr(" Enter course ID to input marks:")
        curses.echo()
        c_id = self.stdscr.getstr().decode("utf-8")
        curses.noecho()
        for student in self.__students:
            self.stdscr.addstr(f"Enter mark for {student.get_name()} ({student.get_id()}): ")
            curses.echo()
            mark = float(self.stdscr.getstr().decode("utf-8"))
            curses.noecho()
            student.set_mark(c_id, mark)
    
    def display_students(self):
        self.stdscr.clear()
        for student in self.__students:
            self.stdscr.addstr(f"ID: {student.get_id()}, Name: {student.get_name()}, DOB: {student.get_dob()}\n")
        self.stdscr.refresh()
        self.stdscr.getch()
    
    def display_courses(self):
        self.stdscr.clear()
        for course in self.__courses:
            self.stdscr.addstr(f"ID: {course.get_id()}, Name: {course.get_name()}, Credits: {course.get_credits()}\n")
        self.stdscr.refresh()
        self.stdscr.getch()
    
    def display_gpa(self):
        self.stdscr.clear()
        for student in self.__students:
            student.calculate_gpa(self.__courses)
            self.stdscr.addstr(f"ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.get_gpa():.2f}\n")
        self.stdscr.refresh()
        self.stdscr.getch()
    def show_mark(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter course ID to show marks: ")
        self.stdscr.refresh()
        curses.echo()
        course_id = self.stdscr.getstr().decode("utf-8")
        curses.noecho()
        for student in self.__students:
            self.stdscr.addstr(f"ID: {student.get_id()}, Name: {student.get_name()}, Marks: {student.get_mark(course_id)}\n")
        self.stdscr.refresh()
        self.stdscr.getch()
    
    def main_menu(self):
        while True:
            self.stdscr.clear()
            self.stdscr.addstr("1. Set number of students\n")
            self.stdscr.addstr("2. Set number of courses\n")
            self.stdscr.addstr("3. Add student\n")
            self.stdscr.addstr("4. Add course\n")
            self.stdscr.addstr("5. Input marks\n")
            self.stdscr.addstr("6. List students\n")
            self.stdscr.addstr("7. List courses\n")
            self.stdscr.addstr("8. Show GPA\n")
            self.stdscr.addstr("9. Show marks\n")
            self.stdscr.addstr("0. Exit\n")
            self.stdscr.addstr("Enter your choice:")
            curses.echo()
            choice = self.stdscr.getch()
            
            if choice == ord('1'):
                self.set_nbstu()
            elif choice == ord('2'):
                self.set_nbc()
            elif choice == ord('3'):
                self.add_student()
            elif choice == ord('4'):
                self.add_course()
            elif choice == ord('5'):
                self.input_marks()
            elif choice == ord('6'):
                self.display_students()
            elif choice == ord('7'):
                self.display_courses()
            elif choice == ord('8'):
                self.display_gpa()
            elif choice == ord('0'):
                break

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: University(stdscr).main_menu())
