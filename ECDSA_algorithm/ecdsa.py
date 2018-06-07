import random
""" additon point a with point b in ecdsa modulo p """
def ecdsa_add(point_elip_a,point_elip_b,p):
    ms_invert = pow(point_elip_b[0]-point_elip_a[0],p-2,p)
    print ms_invert
    c = ((point_elip_b[1]-point_elip_a[1])*ms_invert) % p
    rx = (c**2 - point_elip_a[0]-point_elip_b[0]) % p
    ry = (c*(point_elip_a[0]-rx) - point_elip_a[1]) % p
    return (rx,ry)

""" ecdsa mul scalar with elip curver is y^2 = X^3 + 7
 point_elip is point in eliptic 
 a is a mutiple scalar
 p is modulo"""
def ecdsa_mul(point_elip,a,p):
    if a == 1:
        return point_elip
    if a == 2:
        ms_invert = pow(2*point_elip[1],p-2,p)
        c = ( (3 * point_elip[0]**2) * ms_invert ) % p
        rx = ( c**2 - 2*point_elip[0] ) % p
        ry = ( c*(point_elip[0] - rx) -point_elip[1] ) %p
        return (rx,ry)
    if a > 2:
        return ecdsa_add(point_elip,ecdsa_mul(point_elip,a-1,p),p)
""" sign data z with basepoint G , order basepoint n , private key d, modular p """
def ecdsa_sign(z,G,n,d,p):
    r = 0
    C = 0
    while True:
        k = random.randint(1,n-1)
        C = ecdsa_mul(G,k,p)
        r = C[0] % n
        if r ==0:
            continue
        else:
            k_1 = pow(k,n-2,n)
            s = ( (z + r*d) * k_1 ) % n
            if s == 0:
                continue
            else :
                return (r,s)
""" verify sign (r,s) of data z with public key Q , basepoint G, order basepoint n , modulo p"""
def ecdsa_verify(z ,r,s, Q,G,n,p):
    if r < 1 or r > n -1 or s <1 or s > n -1:
        return False
    w = pow(s ,n -2 ,n )
    u = (z*w)%n
    v = (r*w) %n
    uG = ecdsa_mul(G,u,p)
    vQ = ecdsa_mul(Q,v,p)
    C = ecdsa_add(uG,vQ,p)
    if r == C[0] % n:
        return True
    else:
        return False
p = 67
z =17
n = 79
G = (2,22)
d = 2 # private key
r , s = ecdsa_sign(z,G,n,d,p)
# gen pub key
Q = ecdsa_mul(G,d,p)
print('private key:('+ str(Q[0])+','+str(Q[1])+')')
print('r = ' + str(r) + ' s = '+str(s))
print(ecdsa_verify(z,r,s,Q,G,n,p))

# p = (6,25)
# q = (2,22)
# m = 67
# print ecdsa_add(p,q,m)