#Make a list of your name, weight and height for BMI check.
bmi_elements = ['', 0.0, 0.0]
bmi_messages = ['name', 'weight(kg)', 'height(m)']

#Type three items.
num = 0
for entry in bmi_messages :
    bmi_elements[num] = input('Type your ' + entry + ': ')
    num = num + 1

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
