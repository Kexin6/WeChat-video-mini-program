listU = ['a','B','c','D','e']
r = filter(lambda x : False if x >= 'a' and x <= 'z' else True, listU)
print(list(r))

import time
print(time.time())