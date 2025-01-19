#firsst define a function to 
def drawBorder(width ,  height):
  #if width and height is less then 1 then retuen as a wrong input 
    if width < 2 or height < 2:
        return "wrong input"
    # print this first linne as 
    print('+'+('-'*(width - 2))+'+')
  # print this middle line
    for i in range(height - 2):
      
        print('|'+(' '*(width - 2)) + '|')
      #print last line
    print('+' + ('-' * (width - 2)) + '+')
