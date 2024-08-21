#create a program who reads the input and says the primitive type of the input and all information about it

n = input("Type something: ")
print(f"The type of {n} is {type(n)}")

print(f"Is {n} alphanumeric? {n.isalnum()}")

print(f"Is {n} alpha? {n.isalpha()}")

print(f"Is {n} numeric? {n.isnumeric()}")

print(f"Is {n} decimal? {n.isdecimal()}")

print(f"Is {n} digit? {n.isdigit()}")

print(f"Is {n} only spaces? {n.isspace()}")

print(f"Is {n} lowercase? {n.islower()}")

print(f"Is {n} uppercase? {n.isupper()}")

print(f"Is {n} printable? {n.isprintable()}")

print(f"Is {n} title? {n.istitle()}")

print(f"Is {n} identifier? {n.isidentifier()}")