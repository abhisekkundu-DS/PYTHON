def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 1  # Triangle can be formed
    else:
        return 0  # Triangle cannot be formed

def main_function(arr1,arr2,arr3,n):
    for i in range(n):
        ans = is_triangle(arr1[i],arr2[i],arr3[i])
        print(ans," ")
        
            
            
    
n = int(input())
arr1 = []
arr2 = []
arr3 = []
for _ in range(n):
    a,b,c = map(int,input().split())
    arr1.append(a)
    arr2.append(b)
    arr3.append(c)
    
main_function(arr1,arr2,arr3,n)
