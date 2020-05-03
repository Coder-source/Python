#Your height？(unit [cm])
HEIGHT = 160
print(f'Your height is {HEIGHT} cm.')
print('-----')

#Message of a calculation result
kitchen_message = 'Your optimal kitchen height (No. n) is '

#calculation of a kitchen height (No. 1)
#kitchen height = height[cm] ÷ 2 + 5[cm]

kitchen1 = HEIGHT / 2 + 5
message = kitchen_message.replace('No. n','No. 1')
print(f'{message}{kitchen1} cm.')
print('-----')

#calculation of a kitchen height (No. 2)
#kitchen height = elbow height [cm] - 10[cm]
#It is known that an elbow height is approximately height subtracted by 60 cm.
kitchen2 = HEIGHT - 60 - 10
message = kitchen_message.replace('No. n','No. 2')
print(f'{message}{kitchen2} cm.')
print('-----')