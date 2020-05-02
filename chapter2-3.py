import random


def checkmultiply(num):

    '''

    check the random number is multiply of 3 or 5 or neither

    '''
    if num%3==0 or num%5==0:
        print("%d is 3's or 5's multiply"%num )
    else:
        print("%d is not 3's or 5's multiply" % num)

if __name__ == '__main__':
    num=random.randint(1,100)
    checkmultiply(num)

