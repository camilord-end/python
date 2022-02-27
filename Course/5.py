#main vars
hours= input('Enter Hours:')
rate= input('Enter Rate:')
#var transformation
floatHours= float(hours)
floatRate= float(rate)
#overtime payment check
if floatHours>40:
    regularPay= floatRate*floatHours
    overtimePay= (floatHours-40)*(floatRate*0.5)
    totalPay=regularPay+overtimePay
else:
    totalPay= floatHours*floatRate
#results
print('Pay:',totalPay)