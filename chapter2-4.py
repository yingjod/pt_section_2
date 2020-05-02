def transform(hexchar):
    if hexchar>='0' and hexchar<='9':
        print('the decimal value is',ord(hexchar)-ord('0'))
    elif hexchar <='F' and hexchar >='A':
        print('the decimal value is',ord(hexchar)-ord('A')+10)
    elif hexchar<='f' and hexchar>='a':
        print('the decimal value is',ord(hexchar)-ord('a')+10)
    else:
        print('invalid input')

if __name__ == '__main__':
    hexchar = input('enter a hexchar charecter')
    transform()


