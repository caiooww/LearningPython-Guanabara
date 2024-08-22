#* Manipulating strings

#^ len(), count(), find() | Transformations with replace(), upper(), lower(), capitalize(), title(), strip() | Junction with join()

phrase = input("Enter a phrase: ")

print("The phrase has {} characters".format(len(phrase)))

print("The phrase has {} 'a' characters".format(phrase.count("a")))

print("The first 'a' character is in position {}".format(phrase.find("a")))

print(phrase.replace("a", "e"))

print(phrase.upper())

print(phrase.lower())

print(phrase.capitalize())

print(phrase.title())

print(phrase.strip())

print("-".join(phrase))