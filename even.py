start,end =map(int,(input().split()))
for number in range (start+1,end):
    if number%2 ==0:
        print(number,end ="")
