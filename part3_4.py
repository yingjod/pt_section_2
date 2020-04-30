
def doublefive(num):
    ans = 0
    for i in range(1,num+1):
        if i % 5 == 0 :
            ans += i
    return ans

if __name__ == '__main__':
    num=eval(input())
    doublefive(num)
    print(doublefive(num))
