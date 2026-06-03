# 11-3
# +
from employee import Employee
emp = Employee("a", "b", 1000)
emp.give_raise()
print(emp.salary)
emp.give_raise(2000)
print(emp.salary)
