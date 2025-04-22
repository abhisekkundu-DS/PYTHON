def fahreneite_celsius(arr,n):
    n1 = arr[0]
    for i in range(1,n):
        celsius = ((arr[i]-32)*5)/9
        print(round(celsius)," ")


data = list(map(int,input().split()))
n = len(data)
fahreneite_celsius(data,n)
