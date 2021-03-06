import sys
import kitchen

if len(sys.argv) < 2 :
    print("Designate the name you would like to display")
    sys.exit()

my_name = sys.argv[1]

#Message to display the calculation result
kitchen_message = my_name + "'s optimal kitchen height (No. n) is "

#Your height？(unit [cm])
kitchen_elements = [0.0, 0.0]
kitchen_messages = ['height(cm)', 'current kitchen height(cm)']
#Type the following two items.
num = 0
for entry in kitchen_messages :
    kitchen_elements[num] = input('Type your ' + entry + ': ')
    num = num + 1
print('-----')

try :

#Convert the following information into float ones.
    human_height = float(kitchen_elements[0])
    kitchen_height = float(kitchen_elements[1])

    print(f'Your height is {human_height} cm.')
    print('-----')

#calculation of a kitchen height (No. 1)
#kitchen height = height[cm] ÷ 2 + 5[cm]
    kitchen1 = kitchen.calc1(height = human_height)
    message = kitchen_message.replace('No. n','No. 1')
    print(f'{message}{kitchen1} cm.')
#Compare it with your current kitchen height.
    kitchen.resultmessage(calc_kitchen = kitchen1, now_kitchen = kitchen_height)
    print('-----')

#calculation of a kitchen height (No. 2)
#kitchen height = elbow height [cm] - 10[cm]
#It is known that an elbow height is approximately your height subtracted by 60 cm.
    kitchen2 = kitchen.calc2(height = human_height)
    message = kitchen_message.replace('No. n','No. 2')
    print(f'{message}{kitchen2} cm.')
#Compare it with your current kitchen height.
    kitchen.resultmessage(calc_kitchen = kitchen2, now_kitchen = kitchen_height)
    print('-----')

except ValueError as e :
    print("Review your height or current kitchen height.")
    print(e)
except :
    import traceback
    traceback.print_exc()
