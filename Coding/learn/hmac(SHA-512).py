import hashlib
import hmac

def hmac_calculation(msg, ky):
    return hmac.new((ky.encode()), (str(msg).encode()), hashlib.sha256).hexdigest()

print(hmac_calculation('fzlx', '12345'))