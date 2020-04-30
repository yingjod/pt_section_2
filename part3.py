# i=1
# total=0
# while i <=100:
#     total += i
#     i += 2
# print('total = ',total)

# total = 0
# for i in range(1,101):
#     total+=i
# print('total = ',total)
#
# print('=====')
# for x in range(1,6):
#     print('x = %d'%(x))
#     for y in range(1,6):
#         print('   y = %d'%(y))
#     print('======')

# 9*9 nultiple table
# version 1
for x in range(1,10):
    for y in range(1,10):
        print('%d * %d = %2d'%(y,x,x*y),end=' ')
    print()