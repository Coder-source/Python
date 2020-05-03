#Type your name.
my_name = input('Type your name:') #Plug in the input for the variable.
message = my_name + "'s BMI is "

#BMI = weight[kg]÷(height[m] X height[m])
my_bmi = 50 / (1.6 * 1.6)
print(f'{message}{my_bmi}.')

#Classification of obesity based on your BMI value
if my_bmi < 18.5 :
    print('underweight')
elif my_bmi >= 18.5 and my_bmi < 25 :
    print('Normal range')
elif my_bmi >= 25 and my_bmi < 30 :
    print('Pre-obese')
elif my_bmi >= 30 and my_bmi < 35 :
    print('Obese class I')
elif my_bmi >= 35 and my_bmi < 40 :
    print('Obese class II')
else:
    print('Obese class III')
