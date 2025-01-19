#first define a  function mssort to take a unput two list as a list1 and list2
def mssort(list1 , list2):
  #create an empty list to hold the final sorted result:
        result = []
  # set this starting index as a 0 and in for list1 and i2 for list2
        i1 = 0
        i2 = 0
  #keeping moving up i1 and i2 untill one reaachess the end of its list:
        while i1 < len(list1) and i2 < len(list2):
          # to find the list1 first is smaller then list2
                if list1[i1] < list2[i2]:
                  #add list1 item to the resule
                        result.append(list1[i1])
                  #increment i1
                        i1 += 1
                else:
                  #if  fist element list2 is smaller then reult 
                        result.append(list2[i2])
                  #increment i2
                        i2 += 1
  #if i1 is not at the end of the list add the remaning item
        if i1 < len(list1):
                for j in range(i1, len(list1)):
                        result.append(list1[j])
  # if i2 is not at the end of the list add the remaning item
        if i2 < len(list2):
                for j in range(i2,len(list2)):
                        result.append(list2[j])
      # return the marged sorted list:
        return result

abc  = [4,5,6,7,8,9]
cdf = [1,2,3,10,11]
print(mssort(abc,cdf))
