from Bonus.converter14 import convert
from Bonus.parse14 import parse

feet_inches = input("Enter inches and feet: ")

parsed = parse(feet_inches)
converted = convert(parsed['feet'], parsed['inch'])

print(f"{parsed['feet']} feet and {parsed['inch']} inch is equal to {converted}")
