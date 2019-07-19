a,b1=map(int,input().split())
for num in range(a,b1):
  sum=0
  temp=num
  while(temp>0):
     sum=sum+(temp%10)**3
     temp=temp//10
  if(sum==num):
     print(num,end=" ")
