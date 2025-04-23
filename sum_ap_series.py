def sum_of_ap_series(first,diff,nth):
    total = 0
    for i in range(nth):
        total = total + (first +(i*diff))
    return total
        

def main_calculate(arr1,arr2,arr3,n):
    for i in range(n):
        first = arr1[i]
        diff = arr2[i]
        nth = arr3[i]
        result = sum_of_ap_series(first,diff,nth)
        print(result , " ")
        


n = int(input())
arr1 = []
arr2 = []
arr3 = []
for _ in range(n):
    a,b,c=map(int,input().split())
    arr1.append(a)
    arr2.append(b)
    arr3.append(c)
    
main_calculate(arr1,arr2,arr3,n)
