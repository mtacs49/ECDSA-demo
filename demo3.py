import ecdsa
from ecdsa import SigningKey
from ecdsa import SigningKey, VerifyingKey
import binascii

message = "message"

sk = SigningKey.generate(curve=ecdsa.SECP256k1)

###############################
sk_pem = sk.to_pem()
sk2 = SigningKey.from_pem(sk_pem)
# sk and sk2 are the same key
###############################

vk = sk.get_verifying_key()
vk_pem = vk.to_pem()
vk2 = VerifyingKey.from_pem(vk_pem)


signature = sk2.sign(message)
# signature_str = binascii.hexlify(signature).decode('ascii').upper()
# print signature_str

assert vk2.verify(signature, message) # neu sua message thi se assert loi
