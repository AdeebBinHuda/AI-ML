


def squart(x):
    return x*x
print(squart(5))


# labda_function = lambda x: x*x
# example usage
squart= lambda x: x*x
print(squart(6))

# add
add = lambda x,y: x+y
print(f"Addition is: ",add(5,6))


students = [("John", 25), ("Jane", 22), ("Mike", 30), ("Emily", 28)]
sort= sorted(students, key= lambda x: x[1])
print("after sorted: ",sort)



num= [1,2,3,4,5]
squart= list(map(lambda x: x*x, num))
print(squart)

# filter
num= [1,2,3,4,5]
even = list(filter(lambda x: x%2==0, num))
print(even)


# reduce
from functools import reduce
num= [1,2,3,4,5]
sum= reduce(lambda x,y: x+y, num)
print(sum)

