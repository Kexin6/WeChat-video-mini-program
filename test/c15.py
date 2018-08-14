import  testPack.c14

print('name: ' + __name__)
print('package:' + (__package__ or '当前module不属于任何包'))
print('doc: ' + str(__doc__))
print('file: ' + __file__)