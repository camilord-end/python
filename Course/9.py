str = 'X-DSPAM-Confidence: 0.8475'
newStr = float(str[str.find(':')+1:].strip())
print(newStr)