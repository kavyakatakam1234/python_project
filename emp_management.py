
class Employee:
    def __init__(self, emp_id, emp_name, basic_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary

    def display_details(self):
        print("Employee ID       :", self.emp_id)
        print("Employee Name     :", self.emp_name)
        print("Basic Salary      : ₹", self.basic_salary)

    def calculate_salary(self):
        return self.basic_salary


# Child Class 1
class Developer(Employee):
    def __init__(self, emp_id, emp_name, basic_salary,
                 language, project_name, experience):
                 
        super().__init__(emp_id, emp_name, basic_salary)

        self.language = language
        self.project_name = project_name
        self.experience = experience

    # Method Overriding
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 0.20)

    def display_details(self):
        super().display_details()
        print("Role              : Developer")
        print("Programming Lang. :", self.language)
        print("Project Name      :", self.project_name)
        print("Experience        :", self.experience, "Years")


# Child Class 2
class Manager(Employee):
    def __init__(self, emp_id, emp_name, basic_salary,
                 department, team_size, experience):

        super().__init__(emp_id, emp_name, basic_salary)

        self.department = department
        self.team_size = team_size
        self.experience = experience

    # Method Overriding
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 0.30)

    def display_details(self):
        super().display_details()
        print("Role              : Manager")
        print("Department        :", self.department)
        print("Team Size         :", self.team_size)
        print("Experience        :", self.experience, "Years")


# Child Class 3
class Tester(Employee):
    def __init__(self, emp_id, emp_name, basic_salary,
                 testing_tool, experience, testing_type):

        super().__init__(emp_id, emp_name, basic_salary)

        self.testing_tool = testing_tool
        self.experience = experience
        self.testing_type = testing_type

    # Method Overriding
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 0.15)

    def display_details(self):
        super().display_details()
        print("Role              : Tester")
        print("Testing Tool      :", self.testing_tool)
        print("Experience        :", self.experience, "Years")
        print("Testing Type      :", self.testing_type)


# Main Program

print("===== Employee Management System =====")
print("1. Developer")
print("2. Manager")
print("3. Tester")

choice = int(input("Enter your choice: "))

if choice == 1:

    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    language = input("Enter Programming Language: ")
    project_name = input("Enter Project Name: ")
    experience = int(input("Enter Experience: "))

    emp = Developer(emp_id, emp_name, basic_salary,
                    language, project_name, experience)

elif choice == 2:

    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    department = input("Enter Department: ")
    team_size = int(input("Enter Team Size: "))
    experience = int(input("Enter Experience: "))

    emp = Manager(emp_id, emp_name, basic_salary,
                  department, team_size, experience)

elif choice == 3:

    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    testing_tool = input("Enter Testing Tool: ")
    experience = int(input("Enter Experience: "))
    testing_type = input("Enter Testing Type: ")

    emp = Tester(emp_id, emp_name, basic_salary,
                 testing_tool, experience, testing_type)

else:
    print("Invalid Choice")
    emp = None


if emp is not None:

    print("\n===== Employee Details =====")

    emp.display_details()

    final_salary = emp.calculate_salary()
    bonus = final_salary - emp.basic_salary

    print("Bonus             : ₹", bonus)
    print("Final Salary      : ₹", final_salary)
