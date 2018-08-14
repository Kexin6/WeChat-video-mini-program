from functools import reduce

position = [(2,0), (-2,2), (2,-3)]
r1 = reduce(lambda x,y : position[x][0] + position[y][1], position, 0)
print(r1)

listX = [1,2,3,4,5,6,7,8]
r = reduce(lambda x,y : x + y, listX)
print(r)