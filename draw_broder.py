def drawBorder(width ,  height):
    if width < 2 or height < 2:
        return "wrong input"
    print('+'+('-'*(width - 2))+'+')
    for i in range(height - 2):
        print('|'+(' '*(width - 2)) + '|')
    print('+' + ('-' * (width - 2)) + '+')


abc = drawBorder(10,10)
print(abc)
