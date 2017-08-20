import functions as func

# create file with primes till n, file of str
def calculatePrimes(n, filename = "primes"):
    primes = func.prime(n)

    func.write(primes, filename)