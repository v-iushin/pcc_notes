from employee import Employee
import pytest

@pytest.fixture
def emp():
    e = Employee("a", "b", 1000)
    return e

def test_give_default_raise(emp):
    emp.give_raise()
    assert 6000 == emp.salary

def test_give_custom_raise(emp):
    emp.give_raise(2000)
    assert 3000 == emp.salary