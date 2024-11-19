feet_inches = input("Enter inches and feet: ")

def parse(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inch = float(part[1])
    return {"feet": feet,"inch": inch}


def convert(feet, inch):
    meter = feet * 0.3048 + inch * 0.0254
    return meter


parsed = parse(feet_inches)
converted = convert(parsed['feet'], parsed['inch'])

print(f"{parsed['feet']} feet and {parsed['inch']} inch is equal to {converted}")






