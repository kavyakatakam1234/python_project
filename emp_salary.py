
class Employee:
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter Methods
    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    # Update Salary
    def update_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
            print("Salary Updated Successfully")
        else:
            print("Salary cannot be negative")

    # Add Bonus
    def add_bonus(self, bonus):
        if bonus >= 0:
            self.__salary += bonus
        else:
            print("Bonus cannot be negative")

    # Display Employee Details
    def display_details(self):
        print("Employee Name:", self.__name)
        print("Employee ID:", self.__employee_id)
        print("Salary: ₹", self.__salary)

    # Calculate Annual Salary
    def calculate_annual_salary(self):
        return self.__salary * 12


# Creating Object
emp = Employee("kavya", "201", 30000)

# Display Details
emp.display_details()

# Adding Bonus
emp.add_bonus(5000)

print("\nAfter Bonus:")
print("Salary: ₹", emp.get_salary())

# Updating Salary
emp.update_salary(40000)

print("\nAfter Salary Update:")
print("Salary: ₹", emp.get_salary())

# Annual Salary
print("\nAnnual Salary: ₹", emp.calculate_annual_salary())
