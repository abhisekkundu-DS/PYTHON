import math
def round_divison(arr1,arr2,n1):
    
    for i in range(n1):
        num1 = arr1[i]
        num2 = arr2[i]
        ans = num1 / num2
        if ans > 0:
            print(math.ceil(ans)," ")
        else:
            print(round(ans)," ")

n=int(input())
arr1 = []
arr2 = []
for _ in range(n):
    a,b = map(float,input().split())
    arr1.append(a)
    arr2.append(b)
round_divison(arr1,arr2,n1)
