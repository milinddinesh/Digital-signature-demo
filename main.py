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
        print("Error : "+e)
    return (privateKey, publicKey)

def verify(msg,publicKey,hash):
    print("verify")
    msg_hash = hashlib.sha256(msg.encode("UTF-8")).hexdigest
    hash_decrypt = rsa.decrypt(hash,publicKey).decode("UTF-8")
    print(msg_hash)
    print(hash_decrypt)



try:
    arguments,_ = getopt.getopt(argumentList,options)
    if len(arguments) >1:
        print("You should only specify one option at a time.")
    elif arguments[0][0] == "-e":
        _,value = arguments[0]
        hash = hashlib.sha256((value.encode("UTF-8"))).hexdigest()
        keyGen()
        (privateKey, publicKey) = loadKeys()
        print("Failed")
        sign = rsa.encrypt(hash.encode("UTF-8"),privateKey)
        print("sign: ")
        print(sign)
        verify(hash,publicKey,sign)
except:
    print("something")
