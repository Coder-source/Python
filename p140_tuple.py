#Make a list of your name, weight and height for BMI check.
bmi_elements = ['', 0.0, 0.0]

#Make a tuple about the degree of your obesity
bmi_checks = (
    (0, 18.5, "Be careful about nutrition deficiecny"),
    (18.5, 25, "Maintain your current status"),
    (25, 99, "Plan to improve your nutrition and practice exercise")
)

#Type your name.
bmi_elements[0] = input('Type your name: ')
#Type your weight and height.
bmi_elements[1] = input('Type your weight(kg): ')
bmi_elements[2] = input('Type your height(m): ')

#Display what you typed.
print('Display what you typed for confirmation')
print(f'Name: {bmi_elements[0]}')
print(f'weight and height: {bmi_elements[1:]}')
print('-----')

#Create a message using your name.
message = bmi_elements[0] + "'s BMI is "

#Since your weight and height are string, you need to turn them into float.
my_weight = float(bmi_elements[1])
my_height = float(bmi_elements[2])

#BMI = weight[kg]÷(height[m] X height[m])
my_bmi = my_weight / (my_height * my_height)
print(f'{message}{my_bmi}.')

#Classify the degree of obesity
if my_bmi < bmi_checks[0][1] :
    print(bmi_checks[0][2])
elif my_bmi >= bmi_checks[1][0] and my_bmi< bmi_checks[1][1] :
    print(bmi_checks[1][2])
else :
    print(bmi_checks[2][2])