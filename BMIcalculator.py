height= float(input("Enter the height in meters:"))
weight= float(input("Enter the weight in kilograms:"))
bmi = weight / height*100
print("Your Body Mass Index is:",bmi)
if bmi<18.5:
    print("You are Underweight")
elif bmi<=34.9:
    print("You are Healthy")
elif bmi>=40:
    print("You are Overweight")
else:
    print("You are Obese")
    
