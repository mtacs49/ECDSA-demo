from ecdsa import VerifyingKey, BadSignatureError
vk = VerifyingKey.from_pem(open("public.pem").read())
message = open("message","rb").read()
sig = open("signature","rb").read()
try:
    vk.verify(sig, message)
    print "good signature"
except BadSignatureError:
    print "BAD SIGNATURE"