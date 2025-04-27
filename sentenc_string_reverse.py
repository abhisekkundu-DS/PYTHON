def string_reverse(num):
    n = len(num)
    abc = " "
    for i in range(n):
        abc = abc + num[n-i-1]
    return abc
    
def sentence_reverse(string):
    new_str = string.split()
    le = len(new_str)
    for i in range(le):
        print(new_str[le -1 - i]," ")

    
def main__(abc):
    n1 = len(abc)
    result = ""
    for i in range(n1):
        xyz = string_reverse(abc[i])
        result = result+ xyz+ " "
    return result
