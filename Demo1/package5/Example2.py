origin = 0
def traveller(prePo):
    def go(step):
        nonlocal prePo

        newPo = prePo + step
        prePo = newPo
        return newPo
    return go
test = traveller(origin) #返回闭包函数
print(test(2))
print(test(3))
print(test(6))
