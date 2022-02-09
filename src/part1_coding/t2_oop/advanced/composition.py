from datetime import datetime


class Salary:
    def __init__(self, pay):
        self._pay = pay

    def get_total(self):
        return (self._pay * 12) // 4.9456


class Employee:
    def __init__(self, pay, bonus):
        # self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(pay)

    def annual_salary(self):
        print(datetime.now())
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


if __name__ == '__main__':
    obj_emp = Employee(100, 10)
    print(obj_emp.annual_salary())
