import base64
import string
from exceptions import *
from enums import Algorithms

def xor(string,key=0):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    if type(key) == int:
        ans = ""
        for i in string:
            ans += chr(i ^ key)
    else:
        raise TypeError("key Type Must Be Int.")
    return ans

def b64_en(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b64encode(string).decode('utf-8')

def b64_de(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b64decode(string).decode('utf-8')

def cipher_en(s,key=1):
    if type(key) == str:
        try:
            key = int(key)
        except:
            raise TypeError("Type Should Be 'int'.")
    elif type(key) == int:
        pass
    else:
        raise TypeError("Type Should Be 'int'.")
    
    slow = string.ascii_lowercase + string.ascii_lowercase
    sup = string.ascii_uppercase + string.ascii_uppercase

    ans = ""

    for i in s:
        if i in string.ascii_lowercase:
            ans += slow[slow.index(i) + key]
        elif i in string.ascii_uppercase:
            ans += sup[sup.index(i) + key]
        else:
            ans += i
    
    return ans

def cipher_de(s,key=1):
    if type(key) == str:
        try:
            key = int(key)
        except:
            raise TypeError("Type Should Be 'int'.")
    elif type(key) == int:
        pass
    else:
        raise TypeError("Type Should Be 'int'.")
    
    slow = string.ascii_lowercase + string.ascii_lowercase
    sup = string.ascii_uppercase + string.ascii_uppercase

    ans = ""

    for i in s:
        if i in string.ascii_lowercase:
            ans += slow[slow.index(i) - key]
        elif i in string.ascii_uppercase:
            ans += sup[sup.index(i) - key]
        else:
            ans += i
    
    return ans

def make_enc(alg,key=b""):
    if str(type(alg)) == "<enum 'Algorithms'>":
        if alg.name == Algorithms.XOR.name:
            return [lambda s:xor(s,key),lambda s:xor(s,key)]
        elif alg.name == Algorithms.Base64.name:
            return [lambda s:b64_en(s),lambda s:b64_de(s)]
        elif alg.name == Algorithms.Cipher.name:
            return [lambda s:cipher_en(s,key),lambda s:cipher_de(s,key)]
        else:
            raise AlgorithmError(f"This Algorithm Is Not Available. We Will Be Happy If You Help Us To Make It :)\nGithub : https://github.com/Arshiatmi/Pysha")
    elif type(alg) == list or type(alg) == set:
        ls_en = []
        ls_de = []
        for i in alg:
            if hasattr(i,'name') and i.name == Algorithms.XOR.name:
                ls_en.append(xor)
                ls_de.append(xor)
            elif hasattr(i,'name') and i.name == Algorithms.Base64.name:
                ls_en.append(b64_en)
                ls_de.append(b64_de)
            elif hasattr(i,'name') and i.name == Algorithms.Cipher.name:
                ls_en.append(cipher_en)
                ls_de.append(cipher_de)
            else:
                raise AlgorithmError(f"Type {i} Is Not Supported. Just (Algorithms.Base64/Algorithms.XOR/Algorithms.Cypher) Is Supported.")
        en = ""
        de = ""
        if len(ls_en) == 3:
            en = lambda s:ls_en[2](ls_en[1](ls_en[0](s,key),key),key)
            de = lambda s:ls_de[0](ls_de[1](ls_de[2](s,key),key),key)
        elif len(ls_en) == 2:
            print(ls_en,ls_de)
            en = lambda s:ls_en[1](ls_en[0](s,key),key)
            de = lambda s:ls_de[0](ls_de[1](s,key),key)
        elif len(ls_en) == 1:
            en = lambda s:ls_en[0](s,key)
            de = lambda s:ls_de[0](s,key)
        return en,de
    else:
        raise AlgorithmError(f"This Type Of Algorithm Is Not Supported. Just enum.EnumMeta (Algorithms.Base64/...),list and set Are Supported.")
