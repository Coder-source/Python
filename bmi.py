def calc(weight, height) :
    #BMI = weight[kg] ÷ (height[m] X height[m])
    bmi = weight / (height * height)
    return bmi

def message(bmi) :
    #tuple
    bmi_checks = (
        (0, 18.5, "Be careful about nutritional deficiency."),
        (18.5, 25, "Maintain your current status."),
        (25, 99, "Plan to improve your nutrition and practice exercise.")
    )

    #Classify your degree of obesity based on your BMI value
    if bmi < bmi_checks[0][1] :
        bmi_msg = bmi_checks[0][2]
    elif bmi >= bmi_checks[1][0] and bmi < bmi_checks[1][1] :
        bmi_msg = bmi_checks[1][2]
    else :
        bmi_msg = bmi_checks[2][2]
    
    return bmi_msg