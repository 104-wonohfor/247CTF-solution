

# This file was *autogenerated* from the file crypto/party_ticket.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_0p05 = RealNumber('0.05'); _sage_const_0p5 = RealNumber('0.5'); _sage_const_2 = Integer(2); _sage_const_7 = Integer(7); _sage_const_8 = Integer(8)

import ast

with open("crypto/party_ticket.txt") as f:
    c1, n1, b1 = ast.literal_eval(f.readline().strip())
    c2, n2, b2 = ast.literal_eval(f.readline().strip())


N = n1 * n2
PR = PolynomialRing(Zmod(N), names=('x',)); (x,) = PR._first_ngens(1)

k1 = crt([_sage_const_1 , _sage_const_0 ], [n1, n2])
k2 = crt([_sage_const_0 , _sage_const_1 ], [n1, n2])

f1 = x*(x + b1) - c1
f2 = x*(x + b2) - c2

f = k1*f1 + k2*f2
f = f.monic()

d = f.degree()
beta = _sage_const_1 
epsilon = _sage_const_0p05 
X = ceil(_sage_const_0p5  * N**RR(beta**_sage_const_2  / d - epsilon))

for root in f.small_roots(X=X, beta=beta, epsilon=epsilon):
    r = int(root)
    print(r.to_bytes((r.bit_length() + _sage_const_7 ) // _sage_const_8 , "big").strip(b"\0"))

