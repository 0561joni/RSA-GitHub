import functions as func

def encrypt(message = "hi"):
    encryptedUni = []

    e, n = func.read("publicKey") # store first to lines in e and n

    if isinstance(message, str):
        uniCodeList = func.stringToUnicode(message)

        for x in range(0, len(uniCodeList)):
            encryptedUni.append(func.applyPublicKey(uniCodeList[x], e, n))
    else:
        encryptedUni.append(func.applyPublicKey(message, e, n))

    print("encrypted code:", encryptedUni)
    func.write(encryptedUni, "cryptedMessage")

