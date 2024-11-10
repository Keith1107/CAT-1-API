




         #student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  


    def add_assignment(self, assignment_code, grade):
        self.assignments[assignment_code] = grade
        print(f"Added assignment {assignment_code} with grade {grade} for {self.name}.")


    def display_grades(self):
        if not self.assignments:
            print(f"{self.name} has no grades recorded.Sorry!")
        else:
            print(f"Grades for {self.name}:")
            for code, grade in self.assignments.items():
                print(f"- {code}: {grade}")



# instructor class
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} to the {self.course_name} course.")



    def assign_grade(self, student_id, assignment_code, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_code, grade)
                break
        else:
            print("This student was not found in the system sorrry.")



    def display_all_students_and_grades(self):
        if not self.students:
            print(f"There are no students enrolled in {self.course_name}.")
        else:
            print(f"Here are the students nnames and their grades in {self.course_name}:")
            for student in self.students:
                student.display_grades()




if __name__ == "__main__":
    instructor = Instructor("Dr. Smith", "BBIT")

          #students and their ID
    students_data = [
        ("Mwaura", 101),
        ("Ronaldo", 102),
        ("Odhiambo", 103),
        ("Njore", 104),
        ("Brian", 105),
        ("Trevoh", 106),
        ("Stevo", 107),
        ("Victor", 108),
        ("Simiyu", 109)
    ]

    for name, student_id in students_data:
        instructor.add_student(Student(name, student_id))


    # Assignments and assignment codes
    assignments = {
        "API1": "API Assignment 1",
        "VA02": "Vectors Assignment 2",
        "CA01": "Calculus Assignment 1",
        "IES1": "Introduction to Economics & Statistics Assignment"
    }

    #displaying the main menu and getting user input from the user
    while True:
        print("\nKeith's Online Course Management System")
        print("1. Display all students and grades")
        print("2. Assign a grade to a student")
        print("3. Exit")
        choice = input("Choose one option to continue between 1-3: ")

        if choice == '1':
            instructor.display_all_students_and_grades()

        elif choice == '2':
            student_id = int(input("Please enter the student's ID number to assign them a grade: "))
            print("Available assignments:")
            for code, name in assignments.items():
                print(f"{code}: {name}")
            assignment_code = input("Please enter the assignment code of the assignment to assign this student an assigment: ")
            grade = input("Enter the grade between (A, B, C, D, E): ").upper()
            
            if assignment_code in assignments and grade in ['A', 'B', 'C', 'D', 'E']:
                instructor.assign_grade(student_id, assignment_code, grade)
            else:
                print("Invalid assignment code or grade. Sorry Try Again.")

        elif choice == '3':
            print("Thank you for using my system.Byee!!!!!!!!!!!!!!!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 3 and Try again")
