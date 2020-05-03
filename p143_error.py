my_weight = 50 # weight = 70 kg
my_height = 0 # height = 0 m
try :
#When your height is equal to or less than 0
    if my_height <= 0 :
        raise ValueError("Your height is wrong.")
    #BMI = weight[kg] ÷ (height[m] X height[m])
    my_bmi = my_weight / (my_height * my_height)
    print(f"Your BMI value is {my_bmi}.")
except ValueError as e :
    print("Review your weight or height.")
    print(e)
except :
    import traceback
    traceback.print_exc()
