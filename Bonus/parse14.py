def parse(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inch = float(part[1])
    return {"feet": feet, "inch": inch}
