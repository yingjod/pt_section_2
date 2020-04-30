def count(n):
    total=0
    for i in range(n,2,-2):
        total += (i-2)/i
    return total

if __name__ == '__main__':
    n=eval(input())
    count(n)
    print('total = %.5f'%(count(n)))