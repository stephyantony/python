num2=int(input())
if(num2==0):
  for prod in range(0,5):
    print(0,end=" ")
else:
  for prod in range(1,6):
    print(prod*num2,end=" ")
