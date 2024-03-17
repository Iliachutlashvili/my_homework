

class Employee:

    raise_amount = 1.05


    


    def __init__(self, firstname, lastname, salary):

        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary    
    
    def mail(self):
        return f'{self.firstname[0].lower()}.{self.lastname()}@gmail.com'
    
    def apply_rise(self):
        self.salary = int(self.salary * self.raise_amount)


employee1 = Employee("nika", "vigaca", 4000)

print(employee1.salary)
print(employee1.mail)
employee1.apply_rise()
print(employee1.salary)