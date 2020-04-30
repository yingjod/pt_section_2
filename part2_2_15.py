

def sort(num1,num2,num3):
    """
        this function will sort 3 numbers
    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1

    print('The sorted numbers are',num1 ,num2 ,num3)


if __name__ == '__main__':
    num1, num2, num3 = eval(input('Enter three integers : '))
    sort(num1,num2,num3)
