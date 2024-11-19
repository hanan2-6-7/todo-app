#BMI calculator

weight = float(input("Please Enter your weight(kg)? "))
height = float(input("Please Enter your Height(m)? "))

bmi = round(weight / height**2, 2  )

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, Underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, Normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, Obese.")
else:
    print(f"Your BMI is {bmi}, Clinivally obese.")


