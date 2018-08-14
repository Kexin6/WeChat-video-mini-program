'''
    goal:把所有东西转化成gold
    注意：每个func都叠加了上一个的消耗所以L4ToL为最后答案
'''

from value import *


def L1Tol3(gold, vit):
    expense = l1Tol3 * l1Value + l1Tol3 * l1ValueDiamond * 0.05
    expense += (gold + vit)
    return expense

def L3Tol4(gold, vit):
    #If succeed
    exp1 = l3Tol4 * (l1Value + l1ValueDiamond * 0.05)
    exp1 += gold
    #may fail, so
    expense = exp1 / l3Tol4Rate
    #体力不受到消耗所以不用除以概率
    expense += vit
    return expense

def L4ToL6(gold, vit):
    oneToThree = L1Tol3(l1Tol3Gold, l1Tol3Vit)
    ThreeToFour = L3Tol4(l3Tol4Gold, l3Tol4Vit)
    expense = l4TOl6 * (oneToThree + ThreeToFour)
    expense += (gold + vit)
    return expense


FourToSix = L4ToL6(l4TOl6Gold, l4TOl6Vit)
if FourToSix > 750 :
    print("合成消耗：" + str(FourToSix) + "金, 所以合成不划算，买划算")
else:
    print("合成划算")



