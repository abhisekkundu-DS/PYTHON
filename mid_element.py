def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr

def main_median_calculate(arr,n):
    for i in range(n):
        new_arr = arr[i]
        sort_new_arr = bubble_sort(new_arr)
        len_arr = len(new_arr) - 1
        start = 0
        mid = (start + len_arr)//2
        mid_ele = sort_new_arr[mid]
        print(mid_ele," ")
        
    
    
    
    
    
n  = int(input())
arr = []
for _ in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
main_median_calculate(arr,n)
