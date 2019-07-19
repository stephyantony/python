s,d=map(int,input().split())
for k in range (s+1,d):
    for g in range(2,k):
      if (k%g==0):
        break
    else:
        print(k,end=' ')
