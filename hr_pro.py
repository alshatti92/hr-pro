# from curses import ACS_GEQUAL
# from unicodedata import name


from multiprocessing import managers


class Employee:
    def __init__(self, name, age, salary, employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def get_annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"employee name is {self.name} and he/she is {self.age} years old , he/she has {self.employment_years} years of experience and the current salary {self.salary}"


employee_one = Employee("abdullah", 30, 1000, 7)
print(employee_one.get_annual_salary())
# employees = [Employee("abdullah", 30, 1000, 10), Employee(
#     "mike", 40, 1500, 12), Employee("john", 52, 500, 20), managers]


class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
        return f"employee name is {self.name} and he/she is {self.age} years old , he/she has {self.employment_years} years of experience and the current salary is {self.salary} and the manager bonus precentage is {self.bonus_percentage}%"


# managers = [Manager("jassim", 58, 4500, 25, 2), Manager(
#     "majid", 39, 4000, 12, 3), Manager("saleem", 55, 5000, 20, 4)]

employee_two = Manager("jassim", 58, 4500, 25, 2)
print(employee_two)


# def get_options():
#     return ["Show Employees", "Show Managers", "Add An Employee", "Add An Managers", "Exit"]


# def show_options(options):
#     print()
#     print("Options:")

#     for idx, option in enumerate(options, start=1):
#         print(f"{idx}. {option}")
#     print()


# def add_employee():
#     return {
#         "name": input("name: "),
#         "age": int(input("age: ")),
#         "salary": int(input("salary: ")),
#         "experience": int(input("Employment years: ")),
#     }


# def add_manager():
#     return {
#         "name": input("name: "),
#         "age": int(input("age: ")),
#         "salary": int(input("salary: ")),
#         "experience": int(input("Employment years: ")),
#         "bonus": int(input("Bonus Percentage: "))
#     }


# def main():
#     print("Welcome to HR Pro")

#     options = get_options()
#     if options == 1:
#         print(employees())
#     elif options == 2:
#         print(managers())
#     elif options == 3:
#         return add_employee
#     elif options == 4:
#         return add_manager
#     else:
#         print("leaving HR Pro ... ")


def main():
    employees_list = []
    managers_list = []

    print('''Welcome to HR Pro
          options:
          1. show employees
          2. show managers
          3. add an employee
          4. add a manager
          5. exit ''')

    choice = int(input("pick one "))
    while choice != 5:

        if choice == 1:
            for employee in employees_list:
                print(employee)
        elif choice == 2:
            for manager in managers_list:
                print(manager)
        elif choice == 3:
            employee = Employee(input("Enter the employee name: "), int(input("cham 3omrah? ")), int(
                input("how much the salary? ")), int(input("how many years of expereince? ")))
            employees_list.append(employee)
            print("Victim added successfully")
            print(employee)
        elif choice == 4:
            manager = Manager(input("Enter the employee name: "), int(input("cham 3omrah? ")), int(input("how much the salary? ")), int(
                input("how many years of expereince? ")), float(input("how much bonus you will give him? ")))
            managers_list.append(manager)
            print("Dictator added successfully")
            print(manager)
        else:
            print("choose 3adil")

        choice = int(input("pick one"))


if __name__ == '__main__':
    main()
