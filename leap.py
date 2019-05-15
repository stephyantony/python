#enter the year
year=int(input())
if(year>0):
  if(year%4==0):
        print("Yes")
  else:
        print("No")
else:
   print("invalid year")
