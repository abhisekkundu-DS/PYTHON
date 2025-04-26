    sum = 0
    for i in range(n1):
        last_digit = num % 10 
        sum = sum + last_digit * n2
        num = num // 10
        n2= n2 - 1
    return sum

def _main_(arr,n):
    for i in range(n):
        ans = weight_sum(arr[i])
        print(ans," ")
    
    
n = int(input())
arr = list(map(int,input().split()))
_main_(arr,n)   
