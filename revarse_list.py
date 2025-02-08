def revarse_list(num):
    #initilize the first index position
    position = 0
    #initilize the last inex position
    last = len(num)-1
    #if not a empy list
    while position < last:
        #swape this two list element last and first
        num[position],num[last] = num[last],num[position]
        # now position index increment
        position +=1
        # last index dicrement
        last -= 1

    return num

print(revarse_list([5,9,0,12,6,12]))

