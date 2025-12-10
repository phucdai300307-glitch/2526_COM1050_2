#test 1
a, b, c = map(int,input().split())
def kt(a,b,c):
    canh = sorted([a,b,c])
    x, y, z = canh[0], canh[1], canh[2]
    if a == b and b == c:
        print('tam giac deu')
    elif a == b or b == c or c == a:
        print('tam giac can')
    elif x**2 + y**2 == z**2:
        print('tam giac vuong ')
    else:
        print('tam giac thuong')
kt(a,b,c)
#test 2
from math import *
n = int(input())
def kt(n):
 for i in range(2,n):
  cnt = 0
  if n % i == 0:
    while n % i == 0:
       cnt += 1
       n /= i
    if n == 1:
      print(i, cnt, sep = '^')
    else:
      print(i, cnt, sep = '^', end = '*')
kt(n)
#test 3
n = int(input())
if n % 2 == 0:
  print(n + 1)
else:
  print(n + 2)
#test 4
n = int(input())
if n % 3 == 0 and n > 3:
  print('1')
else:
  print('0')