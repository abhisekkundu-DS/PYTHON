def body_mass_count(weight,height):
    BMI = weight / height**2
    return BMI
    
def _main_(arr1,arr2,n):
    for i in range(n):
        ans = body_mass_count(arr1[i],arr2[i])
        if ans >= 30.0:
            print("Obesity"," ")
        elif ans >= 25.0 and ans <= 30.0:
            print("Overweight"," ")
        elif ans >= 18.5 and ans <= 25.0 :
            print("Normal weight"," ")
        else:
            print("Underweight"," ")
        


n = int(input())
arr1 = []
arr2 = []
for _ in range(n):
    a,b = map(float,input().split())
    arr1.append(a)
    arr2.append(b)
    
_main_(arr1,arr2,n)
