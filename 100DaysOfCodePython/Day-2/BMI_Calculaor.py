# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = float(input("Height: "))
weight = float(input("Weight: "))

"""
BMI Formula:- BMI = weight/(height*height)

"""
BMI = weight / (height * height)
print(int(BMI))