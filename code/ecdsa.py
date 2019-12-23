from fastecdsa.curve import secp256k1 as Curve
from fastecdsa.point import Point

def double_add(s):
    tmp = 1
    for i in s:
        if i == 'D':
            tmp *= 2
        elif i == 'A':
            tmp += 1
        else:
            break
    return tmp

ecc_p = Curve.p
a = Curve.a
b = Curve.b

Gx = Curve.gx
Gy = Curve.gy
G = Point(Gx, Gy, curve=Curve)
d = 705058

Q = d*G
P1 = 4*G
P2 = 5*G
print("base:",G.x,",",G.y)

print("1:",P1.x,",",P1.y)

print("2:",P2.x,",",P2.y)

print("3:",Q.x,",",Q.y)

P4 = "DDADDADADDDDDADDDDADDDDAD"

if double_add(P4) == d:
    print("4:",P4)
