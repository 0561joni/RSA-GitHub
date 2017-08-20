#RSA encrypt decrypt
#-------------------
from KeyGeneration import keyGen as keyGen
from KeyGeneration import calcPrimes as calcPrimes


#calcPrimes.calculatePrimes(1000000000) # takes 24s for 1 billion
print(keyGen.generateKeys()) # about 3s for primes up to 1 billion

