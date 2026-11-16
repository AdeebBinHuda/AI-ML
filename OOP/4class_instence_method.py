class Employee:
    company_name= "Sumalian high school"
    def __init__(self, name ,selery):
        self.name= name
        self.selery = selery

    def display_info(self):
        print(f"Employee name: {self.name}, |Employee selery: {self.selery}")

    @classmethod
    def change_company_name(cls, name):
        cls.company_name= name
    
obj1= Employee("Ali", 50000)
obj1.display_info()
print(f"Company name: {obj1.company_name}")