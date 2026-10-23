from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name=name        
        self.emp_id=emp_id

    def show_info(self):
        print(f'이름 : {self.name}, 사번 : {self.emp_id}')

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id, )
        self.monthly_salary=monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_wage, hours):
        super().__init__(name, emp_id)
        self.hourly_wage=hourly_wage
        self.hours = hours

    def calculate_salary(self):
        return self.hourly_wage*self.hours