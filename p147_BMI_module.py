import bmi
#Type your weight and height
my_weight = 50
my_height = 1.6
#Perform calculation using your BMI module.
my_bmi = bmi.calc(my_weight, my_height)
print(my_bmi)
#Choose a message using your BMI module.
bmi_message = bmi.message(my_bmi)
print(bmi_message)
