class Grandfather:
    def __init__(self,color,lastname):
        self.color= color
        self.lestname= lastname
    def show_module(self):
        print("grandfather like color and his lastname is")


class Fatherclass(Grandfather):
    def __init__(self, hobby, color, lastname):
        super().__init__(color, lastname)
        self.hobby= hobby
    def father_module(self):
            print("father like color and his lastname is")


class Sonclass(Fatherclass, Grandfather):
    def __init__(self,fashion):
        self.fashion= fashion


sc= Sonclass("fashionable")
sc.show_module()   
sc.father_module()       

#gf= Grandfather("yellow", "shams")
#f1 = Fatherclass("reading","blue", "shams")
#print(f"father also like {f1.color} color and his lastname is {f1.lestname} and his hobby is {f1.hobby}")

