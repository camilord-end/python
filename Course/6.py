#main vars
hours= input('Enter Hours:')
rate= input('Enter Rate:')
#var transformation with exeption management
try:
    floatHours= float(hours)
    floatRate= float(rate)
except:
    print('Please enter numbers for the variables')
    quit()
#overtime payment check
if floatHours>40:
    regularPay= floatRate*floatHours
    overtimePay= (floatHours-40)*(floatRate*0.5)
    totalPay=regularPay+overtimePay
else:
    totalPay= floatHours*floatRate
#results
print('Payment:',totalPay)