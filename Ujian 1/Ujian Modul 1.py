# # NO 1

# def Hashtag(string):

#     space = ''
#     hashtag = '#'
#     maxword = 140
#     string2 = string.title()
#     word = string2.split()
#     word2 = space.join(word)
#     word3 = hashtag + word2
    
#     if string == '':
#         print('False')
#     elif len(string) < maxword :
#         print(word3)
#     else :
#         print('False')

# Hashtag(" Hello there how are you doing")
# Hashtag(" Hello World " )
# Hashtag("")

# # NO 2

# def create_phone_number(number):
#     n = number
#     if len(n) == 10 :
#         print('({}{}{}) {}{}{}-{}{}{}{}' .format(n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8], n[9]))
#     else :
#         print('False')

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# # NO 3

# def Sort_odd_even(num):
#     idx = []
#     val = []
#     idxodd = []
#     valodd = []
#     idxevn = []
#     valevn = []

#     for idx, val in enumerate(num):
#         if val %2 != 0:
#             idxodd.append(idx)
#             valodd.append(val)
#         else :
#             idxevn.append(idx)
#             valevn.append(val)
        
#         valodd.sort()
#         valevn.sort(reverse = True)

#     idxtoval = [i for i in range(len(num))]
#     for idx, val in zip(idxodd, valodd):
#         idxtoval[idx] = val
#     for idx, val in zip(idxevn, valevn):
#         idxtoval[idx] = val
    
#     print(idxtoval)

# Sort_odd_even([5, 3, 2, 8, 1, 4])

# # NO 5 

# def hollow_triangle(height):
#     n = height
#     for row in range(1, n+1):
#         for col in range(1, n*2):
#             if row == n or row + col == n+1 or col - row == n-1:
#                 print('#', end = '')
#             else:
#                 print(end = '_')
#         print()
# hollow_triangle(1)
# hollow_triangle(2)
# hollow_triangle(3)
# hollow_triangle(4)
# hollow_triangle(5)
# hollow_triangle(6)
