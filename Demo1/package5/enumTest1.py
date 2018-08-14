from enum import Enum

class VIP (Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1 (Enum):
    YELLOW = 1
    YELLOWALIAS = 1
    BLACK = 3
    RED = 4

print(VIP.GREEN)
print(VIP.GREEN.name)
print(VIP.GREEN.value)
print(VIP['GREEN'])
for vip in VIP:
    print(vip)

print("\n\n")
print(VIP.YELLOW == VIP.GREEN)
print(VIP1.YELLOW == VIP1.YELLOWALIAS)
print(VIP.YELLOW == 1)
print(VIP.YELLOW == VIP1.YELLOW)
print(VIP.YELLOW == VIP.YELLOW)
print("\n")
for vip in VIP1:
    print(vip)

print("\n")
for vip in VIP1.__members__:
    print(vip)

print("\n")
for vip in VIP1.__members__.items():
    print(vip)
