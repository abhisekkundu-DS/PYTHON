def generate_sequence(num):
    list = [0,0]
    for i in range(1,num):
        first_ele = i*2
        sec_ele = i
        list = list + [first_ele,sec_ele]
    return list

print(generate_sequence(10))