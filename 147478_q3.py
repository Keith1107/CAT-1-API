


#employee class
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary


    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")



    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated for {self.name}. New salary: {self.salary}")




#department class
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []



#addding an employee to a department
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"We have added {employee.name} to the {self.department_name} department.")


#calculating the total salary expendituree
    def totalsalaryexpenditure(self):
        total_expenditure = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for the {self.department_name} department is: {total_expenditure}")
        return total_expenditure


#displaying  all employees in a certain department
    def display_all_employees(self):
        if not self.employees:
            print(f"Unfortunately. There are no employees in the {self.department_name} department.")
        else:
            print(f"Employees in the {self.department_name} department include:")
            for emp in self.employees:
                emp.display_details()




#main function
if __name__ == "__main__":
    


    # departments
    departments = {
        "ICT": Department("ICT"),
        "ADMIN": Department("ADMIN"),
        "HR": Department("HR"),
        "FINANCE": Department("FINANCE")
    }


    #employee 
    employees_data = [
        ("Simiyu", 1, 1000000, "ICT"),
        ("Odhiambo", 2, 60000, "ADMIN"),
        ("Wanjiru", 3, 55000, "HR"),
        ("Chalo", 4, 70000, "FINANCE"),
        ("Mboya", 5, 65000, "ICT"),
        ("Cheptoo", 6, 60000, "HR")
    ]

    # Adding employees to departments
    for name, emp_id, salary, dept_name in employees_data:
        if dept_name in departments:
            departments[dept_name].add_employee(Employee(name, emp_id, salary))







    #displaying the main menu and taking user input 
    while True:
        print("\nKeith's LTD Employee and Department Management System")
        print("1. Display all employees in a department")
        print("2. Update employee salary")
        print("3. Display total salary expenditure for a department")
        print("4. Exit Keith's LTD System")
        choice = input("Please choose an option to continue (1-4): ")





              #choice 1
        if choice == '1':
            dept_name = input("Please enter the department name you want to continue (ICT, ADMIN, HR, FINANCE): ").upper()
            if dept_name in departments:
                departments[dept_name].display_all_employees()
            else:
                print("Sorry, Invalid department name. Try again.")



       #choice 2
        elif choice == '2':
            emp_id = int(input("Please enter the employee ID to update salary - ID(1-6): "))
            new_salary = int(input("Enter the new salary for this employee: "))
            for dept in departments.values():
                for emp in dept.employees:
                    if emp.employee_id == emp_id:
                        emp.update_salary(new_salary)
                        break
                else:
                    continue
                break
            else:
                print("Sorry employee not found. Try Again")



                      #choice 3
        elif choice == '3':
            dept_name = input("Please enter the department name (ICT, ADMIN, HR, FINANCE): ").upper()
            if dept_name in departments:
                departments[dept_name].calculate_total_salary_expenditure()
            else:
                print("Sorry, Invalid department name. Try Again.")


                     #last choice 
        elif choice == '4':
            print("Sad to see you leave. We hope to see you again soon.!!!!")
            break

        else:
            print("Error: Invalid input - Please enter a number between 1 and 4 and Try Again")
