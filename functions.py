from itertools import chain
import numpy as np


# write file of str from int list
def write(numbersToStore, filename = "newFile"): #does only work with numbers, no letters
    fileContent = open(filename, "w")

    if type(numbersToStore) in (tuple,list):
        for x in range(0, len(numbersToStore)):
            fileContent.write(str(numbersToStore[x]))
            fileContent.write("\n")
        fileContent.close()

    elif type(numbersToStore) == np.ndarray:
        numbersToStore.tofile(filename, "\n")

    elif type(numbersToStore) in (str, chr):
        fileContent.write(numbersToStore)
        fileContent.close()

    elif type(numbersToStore) == int:
        fileContent.write(str(numbersToStore))
        fileContent.close()

    else:
        print("datatype to write in file:", filename, "is unknown")
        fileContent.close()

# read file of str, return list
def read(filename = "newFile"):
    with open(filename, "r") as strPrimesInFile:
        strPrimes = strPrimesInFile.read()  # read file content and safe as str
    strPrimesInFile.close()

    primeList = list(map(int, strPrimes.splitlines()))  # convert str to list (splitline) and int

    return primeList

# calculate prime numbers
def primeSlow(limit):
    primList = []
    zahlen = [True] * (limit + 1)

    # Da 0 und 1 keine Primzahlen sind, werden sie auf False gesetzt
    zahlen[0] = False
    zahlen[1] = False

    i = 2

    while i * i <= limit:
        if zahlen[i] == True:  # Die Zahl i ist als prim markiert
            # Streiche alle Vielfachen von i
            for k in range(i * i, limit + 1, i):
                zahlen[k] = False

        i = i + 1

    # Speichern aller gefundenen Zahlen in primList
    for i, v in enumerate(zahlen):
        if v == True:
            primList.append(i)
    return primList

# claculate primes with numpy much faster
def prime(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(int(n/3 + (n%6==2)), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5/3+1)):
        if sieve[i]:
            k=3*i+1|1
            sieve[      int((k*k)/3)      ::2*k] = False
            sieve[int((k*k+4*k-2*k*(i&1))/3)::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

# factorization return list
def fact(n):
    l = []
    for i in chain([2], range(3, n // 2 + 1, 2)):

        while n % i == 0:
            l.append(i)
            n = n // i  # "//" like int(n/i)
        if i > n:
            break
    return l

# return ggt, x, y
def erwEuklidischerAlgorithmus(a, b):
    aalt = a
    amitte = b
    xalt = 1
    xmitte = 0
    yalt = 0
    ymitte = 1
    while amitte != 0:
        q = aalt // amitte
        aneu = aalt - q * amitte
        xneu = xalt - xmitte * q
        yneu = yalt - ymitte * q
        xalt = xmitte
        xmitte = xneu
        yalt = ymitte
        ymitte = yneu
        aalt = amitte
        amitte = aneu

    return (aalt, xalt, yalt)

# convert string (to char) to unicode, return list of unicode from each character
def stringToUnicode(text):
    charList = list(text)
    uniCodeList = []

    for x in range (0, len(charList)):
        uniCodeList.append(ord(charList[x])) # append unicode of each character
        #print(uniCodeList[x])
    return uniCodeList

# convert string to unicode, return list of unicode for standardized bit length
def strToUni(text):
    ... # some code

# convert Unicode to string
def unicodeToString(uniCodeList):
    charList = []
    for x in range (0, len(uniCodeList)):
        charList.append(chr(uniCodeList[x])) # append unicode of each character

    strOfChars = ''.join(charList) # char list to string
    return strOfChars

# encrypt with public key, type(toCrypt) = numbers, e, n
def applyPublicKey(toCrypt, e, n):
    encrypted = pow(toCrypt, e, n)
    #encrypted = (toCrypt ** e) % n
    return encrypted

# decrypt with private key, return unicode
def applyPrivateKey(encrypted, d, n):
    decrypted = pow(encrypted, d, n)
    #decrypted = (encrypted ** d) % n # about 40 times slower
    return decrypted
