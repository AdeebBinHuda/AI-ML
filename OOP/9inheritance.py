class Grandfather:
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