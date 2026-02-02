
class Employee():

  def __init__(self,name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def __str__(self):
    return f"{self.name} {self.age} {self.salary}"

  def afficher(self):
    print("name",self.name)
    print("age", self.age)
    print("salary",self.salary)

em1 = Employee("carl" ,38 , 70000)
em2 = Employee("ali" ,26,20000)
em3 = Employee("emy" , 20 , 24000)

Employees = [em1,em2,em3]


def e_sort(emy):

  return emy.salary

sEmployee = sorted(Employees ,key= e_sort)
print(sEmployee)

for e in sEmployee:
  print(e)
