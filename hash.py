import hashlib
from pathlib import Path
import json
import os

BASE_DIR = Path(__file__).parent
secrets={}

def sig_in(user:str,passs:str):
    try:
        a=hashlib.md5(passs).hexdigest()
        secrets[user] = a
        jj=json.loads(secrets)
        
    except:
        print("Xato")

print(sig_in('Davron',1234))