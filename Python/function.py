# 1. No input, No return
def my_first_function():
    a= 10
    b= 12
    print(a+b)

my_first_function()


# 2. input, no return
def add_two_numbers(a,b):  #argument
    print(a+b)

add_two_numbers(10,24)  # parameters
add_two_numbers(20,35)



# 3. input , return
def multiply_two_numbers(a,b):
    return a*b
value= multiply_two_numbers(12,2)
print(value)

# no input , return
def  hello():
    return "Hello"
greetings= hello()
print(greetings)


# input , return

def add_number(a,b): # arguments
    return a+b

result= add_number(23,5)
print(result)

# NO input , return

def hello():
    return "Hi"
say= hello()
print(say)