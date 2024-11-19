password = input("Enter new password: ")

result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = True

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
result["upper-case"] = upper

print(result)

if all(result.values()): # all checks the value of all result dictionary value is true

    print("Strong password")
else:
    print("Weak password")