# Single inheritence
"""class Grandfather:
    def __init__(self,color,lastname):
        self.color= color
        self.lestname= lastname
    


class Fatherclass(Grandfather):
    def __init__(self, hobby, color, lastname):
        super().__init__(color, lastname)
        self.hobby= hobby     

gf= Grandfather("yellow", "shams")
f1 = Fatherclass("reading","blue", "shams")
print(f"father also like {f1.color} color and his lastname is {f1.lestname} and his hobby is {f1.hobby}")
"""



# Multiple inheritence
class Grandfather:
    def __init__(self,color,lastname):
        self.color= color
        self.lestname= lastname
    def Grandfather_module(self):
        print("grandfather like color and his lastname is")


class Fatherclass(Grandfather):
    def __init__(self, hobby):
        self.hobby= hobby
    def father_module(self):
            print("father like color and his lastname is")


class Sonclass(Fatherclass, Grandfather):
    def __init__(self,fashion,hobby, color,lastname):
        self.fashion= fashion
        Fatherclass.__init__(self,hobby)
        Grandfather.__init__(self,color, lastname)

sc= Sonclass("fashionable", "reading", "blue", "shams")
print(sc.fashion,sc.hobby, sc.color, sc.lestname)
sc.Grandfather_module()   
sc.father_module()       

#gf= Grandfather("yellow", "shams")
#f1 = Fatherclass("reading","blue", "shams")
#print(f"father also like {f1.color} color and his lastname is {f1.lestname} and his hobby is {f1.hobby}")






# Multilevel inheritence
"""class Grandfather:
    def __init__(self,color,lastname):
        self.color= color
        self.lestname= lastname
    def Grandfather_module(self):
        print("grandfather like color and his lastname is")


class Fatherclass(Grandfather):
    def __init__(self, hobby, color, lastname):
        super().__init__(color, lastname)
        self.hobby= hobby
    def father_module(self):
            print("father like color and his lastname is")


class Sonclass(Fatherclass, Grandfather):
    def __init__(self,fashion,hobby, color,lastname):
        self.fashion= fashion
        super().__init__(hobby, color, lastname)


sc= Sonclass("fashionable", "reading", "blue", "shams")
print(sc.fashion,sc.hobby, sc.color, sc.lestname)
sc.Grandfather_module()   
sc.father_module()       

"""