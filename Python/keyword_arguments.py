def user_details(f_name,l_name,age):
    print(f"my name is {f_name} also last name part is {l_name}. i am {age} years old")

user_details(age= 27,l_name="hasan",f_name= "alif")



# arbetary numbers of keywords arguments
def user_details(**kwargs):   # **data
    print(kwargs)
    print(f"My name is {kwargs['name']} {kwargs['last_name']}.I am {kwargs['age']}  years old.")


user_details(name="alik",last_name="hasan",age=26, address="jingura")