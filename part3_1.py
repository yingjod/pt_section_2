

def sum_total(a,b):
    ans = 0
    for i in range (a,b+1):
        ans += i
    return ans

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum_total(a,b)
    print(sum_total(a,b))
