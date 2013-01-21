# Filename: compute_bmi.py
# Author: Lim Ah Seng
# Created: 20130221
# Modified: 20130221
# Description: Program to get user weight and height and
# calculate body mass index

# main

# prompt and get weight
weight = int(input("Enter weight in kg: "))

# prompt and get height
height = float(input("Enter height in m: "))

# calculate bmi
bmi = weight / (height * height)

# display result
print("BMI = {0:.2f}".format(bmi))
