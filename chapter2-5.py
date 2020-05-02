def checknum(num):
    '''
    check the number is multiple of 5 or 8
    '''
    if (num%5==0 and num%8==0) or (num%5==0 or num%8==0):
        print('%d can be divided by 5 or 8'%num)
        print('%d can be divided by 5 and 8' % num)
    else:
        print('%d can\'t be divided by 5 or 8' % num)


if __name__ == '__main__':
    num = eval(input('enter a number: '))
    checknum(num)

