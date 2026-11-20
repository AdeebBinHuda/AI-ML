class Singleton:
    _instance = None #class variable

    def __new__(cls):
        if cls._instance is None:
            print("1st object is created")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
obj1 = Singleton()
obj2= Singleton()

print(obj1 is obj2)