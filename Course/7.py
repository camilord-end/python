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
def computePay(hours,rate):
    if hours>40:
        regularPayment=hours*rate
        overtimePayment=(hours-40)*(rate*0.5)
        return overtimePayment+regularPayment
    else:
        regularPayment=hours*rate
        return regularPayment
#results
print('Payment:',computePay(floatHours,floatRate))