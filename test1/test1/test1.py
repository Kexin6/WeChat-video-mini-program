#!/usr/bin/env python
# encoding: utf-8
#随机生成200个激活码
__author__ = 'Kxrr'

import random, string

ALL_LETTERS = string.ascii_uppercase + string.digits
codeAmount = 200
codeRound = 10
codeResult = []

while len(codeResult) != codeAmount:
     everyCode =''.join((random.choice(ALL_LETTERS) for i in range(codeRound)))
     if everyCode not in codeResult:
        codeResult.append(everyCode)

print (len(codeResult))
print (codeResult)