from vectors import *

g1 = gP(vector2(0, 0), vector2(1, 2))
g2 = gP(vector2(0, 2), vector2(-1, 3))

print(f"g1: {g1}\ng2: {g2}")
print(vecPar(g1.a, g2.a))
print(g1 |n| g2)