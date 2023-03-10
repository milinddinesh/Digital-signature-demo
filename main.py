
#!/usr/bin/env python3

# A simple python application to demonstrate the use of Digital signature 
# Milind Dinesh

import getopt , sys , hashlib , rsa

argumentList  = sys.argv[1:]
options = "d:e:"

def keyGen():
    (publicKey,privateKey) = rsa.newkeys(1024)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    try:
        with open('keys/publicKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/privateKey.pem', 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())

    except Exception as e:
        print("Error while loading keys : ")
        print(e)
    return (privateKey, publicKey)

#A function just to verify the output . 
def verify(sign , publicKey, message):
    try:
        return rsa.verify(message.encode("UTF-8"),sign,publicKey)
    except : return False

try:
    arguments,_ = getopt.getopt(argumentList,options)
    if len(arguments) >1:
        print("You should only specify one option at a time.")
    elif arguments[0][0] == "-e":
        _,value = arguments[0]
        hash = hashlib.sha256((value.encode("UTF-8"))).hexdigest()
        keyGen()
        (privateKey, publicKey) = loadKeys()
        sign = rsa.sign(value.encode("UTF-8"),privateKey,"SHA-256")
        print("Message : " + value + "\n")
        print("sign")
        print(sign)
        print("\n")
        if verify(sign,publicKey,value):
            print("Authentic")
        else : 
            print("Authenticity check failed")
except Exception as e:
    print("Some error occured: ")
    print(e)
