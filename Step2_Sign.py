from ecdsa import SigningKey
sk = SigningKey.from_pem(open("private.pem").read())
message = open("message","rb").read()
sig = sk.sign(message)
open("signature","wb").write(sig)