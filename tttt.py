def not_love(num):
    """
        this function will take some numbers and returns the smalest one
    :param num:
    :return:
    """
    min_num = num

    while num != 9999:
        num=eval(input())
        if num < min_num:
            min_num = num
    return min_num

if __name__ == '__main__':
    num = eval(input())
    love=not_love(num)
    print(love)