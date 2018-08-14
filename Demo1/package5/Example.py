#用不闭包解决旅行者问题
origin = 0

def go(step):
    global origin #对应下面的origin
    newPo = origin + step
    origin = newPo
    return newPo


print(go(2))
print(go(3))
print(go(6))
