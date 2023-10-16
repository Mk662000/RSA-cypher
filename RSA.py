import math

def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp


p = 3
q = 11
e = 7
msg = 2
n = p*q
phi = (p-1)*(q-1)
print("phi n = ",phi)
print("the original message = ",msg)

while (e < phi):

	# e must be co-prime to phi and
	# smaller than phi.
	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1


def modInverse(E, eN):
 
    for K in range(1, eN):
        D =int((1 + (K*eN))/E)
        if ((D*E)-(1+(K*eN)) == 0):
            return K
    return -1

k = modInverse(e,phi)
print("k = ",k)
d = int((1 + (k*phi))/e)
print("d = ",d)

#Encryption algorithm
enc = int(math.fmod(pow(msg, e), n))
print("encrypted message = ",enc)

#decryption algorithm
dec = int(pow(enc,d))
dec2 = dec%n
print("decrypted message = ",dec2)
# res = enc**d
# res2 = res% n
# print(res2)
