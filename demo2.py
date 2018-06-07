import ecdsa
from ecdsa import SigningKey
from ecdsa import SigningKey, VerifyingKey
import binascii

message = "message"

sk = SigningKey.generate(curve=ecdsa.SECP256k1)

###############################
sk_string = sk.to_string()
sk2 = SigningKey.from_string(sk_string, curve=ecdsa.SECP256k1)
# sk and sk2 are the same key
###############################

vk = sk.get_verifying_key() 
vk_string = vk.to_string()
vk2 = VerifyingKey.from_string(vk_string, curve=ecdsa.SECP256k1)


signature = sk2.sign(message)
# signature_str = binascii.hexlify(signature).decode('ascii').upper()
# print signature_str

assert vk2.verify(signature, message) # neu sua message thi se assert loi
