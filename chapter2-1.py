#
# a,b,c=eval(input('Enter a, b, c :'))
# s1=-b+(b**2-((4*a*c)**0.5))/2*a
# s2=-b-((b**2)-(4*a*c)**0.5)/2*a
#
# print('the solutions are %.6f and %.6f'%(s1,s2))
#

import math

def solution(a,b,c):
    '''

    count Linear equations

    '''
    deter=b**2-4*a*c
    if deter>0:
        answer1=(-b+math.sqrt(deter))/(2*a)
        answer2=(-b-math.sqrt(deter))/(2*a)
        print('the solutions are %.6f and %.6f'%(answer1,answer2))

    elif deter==0:
        answer=-b/(2*a)
        print('the solutions is %.6f'%(answer))
    else:
        print('no solution')


if __name__ == '__main__':
    a, b, c = eval(input('enter a, b, c:'))
    solution(a, b, c)

