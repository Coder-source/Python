def calc1(height) :
    #Calculation of a kitchen height (No. 1)
    #kitchen height = height [cm] ÷ 2 + 5 [cm]
    kitchen = height / 2 + 5
    return kitchen

def calc2(height) :
    #Calculation of a kitchen height (No. 2)
    #kitchen height = elbow height [cm] - 10 [cm]
    #It is known that an elbow height is approximately your height subtracted by 60 cm.
    kitchen = height - 60 -10
    return kitchen

def resultmessage(calc_kitchen, now_kitchen) :
    #tuple
    k_messages = (
        ("Optimal height", "Change the thickness of your slippers for adjustment!!"),
        ("Lower than your optimal height", "Be careful about backache!!"),
        ("Higher than your optimal height", "Be careful about shoulder discomfort!!"),
    )
    #Compare your calculated kitchen height with your current one
    if calc_kitchen == now_kitchen :
        print(k_messages[0][0])
        print(k_messages[0][1])
    elif calc_kitchen > now_kitchen :
        print(k_messages[1][0])
        print(k_messages[1][1])
    else :
        print(k_messages[2][0])
        print(k_messages[2][1])
