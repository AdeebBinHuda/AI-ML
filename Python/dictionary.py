# {}
# Key value pairs
# no indexing
# key are immutable

a= {"azad": 12, "khan": 13, "ali": 14,1: [1,2,3,4,5], 2: 'c'}
print(type(a))  # type of the dictionary
print(len(a))   # len of the dictionary

print(".......")
for i in a.values():
    print(i)

# keys and vlaues
print(a.keys(), a.values())
print("---------")
for k,v in a.items():
    print(f"kay Name: {k} , values {v}")


print("---------")
a= [1,2,3]
b=["Mango", "Banana", "Orange"]
print(list(zip(a,b)))  # zip function
print("---------")
c= dict(zip(a,b))
print(dict(zip(a,b)))  # zip function with dict

print(c[2])
