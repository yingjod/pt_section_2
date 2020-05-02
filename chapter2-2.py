import math

def dis(x1,y1):

    '''
    count it
    '''

    dist=math.sqrt((x1-0)**2+(y1-0)**2)

    if dist<=8:
        print("(%d,%d) is inside of the circle"%(x1,y1))
    else:
        print("(%d,%d) is outside of the circle"%(x1,y1))

if __name__ == '__main__':
    x1, y1 = eval(input())
    dis(x1,y1)
