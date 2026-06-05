import sys
for x in list(map(int, sys.stdin.read().splitlines())):
  if ((x%4==0) and (x%100!=0)) or (x%400==0): #西元年被4整除且不被100整除，或被400整除者即為閏年
    print('閏年')
  else:
    print('平年')
