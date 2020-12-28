import base64
import string
from exceptions import *
from enums import Algorithms
import enum

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

def b64_en(string):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b64encode(string).decode('utf-8')

def b64_de(string):
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
        print(alg,type(alg))
        if alg.name == Algorithms.XOR.name:
            return lambda s:xor(s,key)
        elif alg.name == Algorithms.Base64.name:
            return [lambda s:b64_en(s),lambda s:b64_de(s)]
        elif alg.name == Algorithms.Cipher.name:
            return [lambda s:cipher_en(s,key),lambda s:cipher_de(s,key)]
        else:
            raise AlgorithmError(f"This Algorithm Is Not Available. We Will Be Happy If You Help Us To Make It :)\nGithub : https://github.com/Arshiatmi/Pysha")
    elif type(alg) == list or type(alg) == set:
        for i in alg:
            if type(i) == enum.EnumMeta:
                pass
            else:
                raise AlgorithmError(f"Type {i} Is Not Supported. Just (Algorithms.Base64/Algorithms.XOR/Algorithms.Cypher) Is Supported.")
        pass
    else:
        raise AlgorithmError(f"This Type Of Algorithm Is Not Supported. Just enum.EnumMeta (Algorithms.Base64/...),list and set Are Supported.")
