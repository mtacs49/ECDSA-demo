from ecdsa import SigningKey
import ecdsa

sk = SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()
open("private.pem","w").write(sk.to_pem())
open("public.pem","w").write(vk.to_pem())