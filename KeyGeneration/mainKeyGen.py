#RSA encrypt decrypt
#-------------------
from KeyGeneration import keyGen as keyGen
from KeyGeneration import calcPrimes as calcPrimes

print(keyGen.generateKeys())
#calcPrimes.calculatePrimes(100000000)