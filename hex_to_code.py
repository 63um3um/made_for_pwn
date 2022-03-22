#it need for making shellcode xxd -> hex_to_code
import sys

hexcode = sys.argv[1]

for i in range(0,len(hexcode),2) :
    print('\\x'+hexcode[i:i+2],end = '')

