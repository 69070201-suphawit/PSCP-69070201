"""Temperature"""
Temperature = float(input())
text_1 = input()
text_2 = input()
Temperature_C = ""
if text_1 == 'C' :
    Temperature_C = Temperature
elif text_1 == 'F' :
    Temperature_C = (Temperature - 32) * 5 / 9
elif text_1 == 'K' :
    Temperature_C = Temperature - 273.15
elif text_1 == 'R' :
    Temperature_C = (Temperature - 491.67) * 5 / 9

if text_2 == 'F' :
    Temperature_C = Temperature_C * 9/5 + 32
elif text_2 == 'K' :
    Temperature_C = Temperature_C + 273.15
elif text_2 == 'R' :
    Temperature_C = (Temperature_C + 273.15) * 9/5
print(f'{Temperature_C:.2f}')
