

def sum_even(a,b):
    ans = 0
    for i in range (a,b+1):
        if i % 2 == 0:
            ans += i
    return ans

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum_even(a,b)
    print(sum_even(a,b))

