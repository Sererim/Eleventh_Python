from home import MyStr
from home import Archive
from home import Rectangle

s = MyStr("Hello, World!")
print(s, s.name, s.time)

a = Archive(20, "Hello")
b = Archive(30, "World!")
print(a)
print(b)
print(a.get_data())
print(repr(a))

ABCD = Rectangle(10, 10, None)
DCBA = Rectangle(5, 5, None)
DCAB = Rectangle(100, 100, None)
    
print(ABCD + DCAB)
print(ABCD - DCAB)
print(ABCD * DCBA)
print(DCAB / ABCD)
    
print(f"{ABCD == DCAB = }")
print(f"{ABCD > DCAB = }")
print(f"{ABCD < DCAB = }")
print(f"{ABCD != DCAB = }")

