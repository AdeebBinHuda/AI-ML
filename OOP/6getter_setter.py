class Employee:
    company_name = "TechCop"

    def __init__(self, name, salary):
        self.name= name
        self._salary= salary

    def get_salary(self,password):
        if password== "admin123":
            return self._salary
        else:
            return "Access Denied"

    def set_salary(self, new_salary, password):
        if password== "admin123":
            self._salary= new_salary
            return "Salary updated successfully"
        else:
            return "Access Denied"
        
obj1 = Employee("John", 50000)
obj2= Employee("Alice", 70000)
print(f"Employee name: {obj1.name}, Salary: {obj1.get_salary('admin123')}, Company: {obj1.company_name}")


obj1.set_salary(55000, 'admin123')
print(f"Employee name: {obj1.name}, Salary: {obj1.get_salary('admin123')}, Company: {obj1.company_name}")

obj2.get_salary("wrongpassword")
print(obj2._salary)
print(obj2.get_salary("wrongpassword")) 
 # This will return "Access Denied" since the password is incorrect
