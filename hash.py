import hashlib
import json

secrets={}

def sig_in(user,password):
    try:
        a=hashlib.md5(password).hexdigest()
        return a
        
    except  Exception as e:
        print(f"{e}")

print(sig_in('Davron',123))

