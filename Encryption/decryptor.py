import functions as func
from definitions import PRIVATE_KEY_PATH

def decrypt(filename = "cryptedMessage"):
    encryptedUni = func.read(filename)
    decryptedUni = []

    d, n = func.read(PRIVATE_KEY_PATH)  # store first to lines in d and n

    if len(encryptedUni) > 1:
        for x in range(0,len(encryptedUni)):
            decryptedUni.append(func.applyPrivateKey(encryptedUni[x], d, n))
    else:
        decryptedUni.append(func.applyPrivateKey(encryptedUni[0], d, n))

    strDecrypted = func.unicodeToString(decryptedUni)
    print("decrypted code:", strDecrypted)