from functools import reduce


l = [1,2,3,4,5,6,7,13,2,3,4,5,67]

# def greatest(a,b):
#     if a<b:
#         return b
#     else:
#         return a

print(reduce(max,l))#max is inbult function 

