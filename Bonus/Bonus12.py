# feet_inches = "5 12"
# print(feet_inches.split(" "))  # slices at the space
# greeting = "hey-me-you"
# print(greeting.split("-"))  # slices at the -


feet_inches = input("Enter your height.")


def convert(feet_inches):
    feet_inches = feet_inches.split(" ")
    feet = float(feet_inches[0])
    inche = float(feet_inches[1])
    meter = feet * 0.3048 + inche * 0.0254
    return f"{feet} feet {inche} incs is equal to{meter} meters."

print(convert(feet_inches))
