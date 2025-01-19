def reverseString(text):
...     text = list(text)
...     for i in range(len(text)//2):
...# using loop to access number of elemment for half of  order
...
...     #fswap the values of i and its
...         mirrorIndex = len(text) -1 - i
#swape number in 2 index  i and mirror index
...         text[i] , text[mirrorIndex] = text[mirrorIndex] , text\[i]
# join this multiple  string to a single string 
...     return ' '.join(text)
...
