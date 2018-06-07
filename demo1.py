import ecdsa
from ecdsa import SigningKey
import binascii

message = "message"

sk = SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key() 

# key = binascii.hexlify(sk.to_string()).decode('ascii').upper()
# print key # 64 bytes

signature = sk.sign(message)
# signature_str = binascii.hexlify(signature).decode('ascii').upper()
# print signature_str

assert vk.verify(signature, message) # neu sua message thi se assert loi
