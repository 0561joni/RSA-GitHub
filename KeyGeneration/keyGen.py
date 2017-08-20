import random
import functions as func
from definitions import PUBLIC_KEY_PATH
from definitions import PRIVATE_KEY_PATH

#primList = func.prime(100000000)  # just for testing..
# if primes file doesnt exist, write it
try:
    primList = func.read("primes")
except:
    func.write(func.prime(10000000), "primes")
    primList = func.read("primes")

# generate public and private key and write to separate files

def generateKeys():  # return e, d, n

    # ---public---
    random.seed  # picks 2 primes from list
    pIndex = random.randint(int(9 / 10 * len(primList)), len(primList) - 1)
    qIndex = random.randint(int(9 / 10 * len(primList)), len(primList) - 1)
    while pIndex == qIndex:
        pIndex = random.randint(int(9 / 10 * len(primList)), len(primList) - 1)
        qIndex = random.randint(int(9 / 10 * len(primList)), len(primList) - 1)

    # set primes p and q
    p = primList[pIndex]
    q = primList[qIndex]

    # n
    n = p * q
    phi = (p - 1) * (q - 1)

    factorized = func.fact(n)

    # find e that is not a prime factor of n
    isFactor = True

    while (isFactor):
        random.seed
        e = primList[random.randint(int(9 / 10 * len(primList)), len(primList) - 1)]  # random element from primList
        isFactor = False

        for i in range(0, len(factorized)):
            if factorized[i] == e:  # check if e is primefactor of phi
                isFactor = True

    # ---private---
    (ggt, x, y) = func.erwEuklidischerAlgorithmus(e, phi)

    if ggt > 1:
        d = -1
    else:
        if x < 0:
            x = x + phi
        d = x

    # ---write---
    # only for mac:
    #func.write([e, n], "/Users/mac/Documents/GitHub/RSA-GitHub/Encryption/publicKey")
    #func.write([d, n], "/Users/mac/Documents/GitHub/RSA-GitHub/Encryption/privateKey")
    # write to main folder:
    #func.write([e, n], "publicKey")
    #func.write([d, n], "privateKey")
    # general solution:
    func.write([e, n], PUBLIC_KEY_PATH)
    func.write([d, n], PRIVATE_KEY_PATH)

    return e, d, n