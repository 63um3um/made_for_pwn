string = input('input string : ')

result = ''
for i in range(len(string)-1,-1,-1) :
    result += str(hex(ord(string[i])))[2:]
print('0x'+result)
