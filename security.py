import base64
import string
from exceptions import *
from enums import Algorithms
from pickle import Unpickler,Pickler

class Crypto:
    def __init__(self,enc_ls,dec_ls,key):
        self.enc_ls = enc_ls
        self.dec_ls = dec_ls
        self.key = key

    def __call__(self,s):
        t_enc = s
        for i in self.enc_ls:
            t_enc = i(t_enc,self.key)
        return t_enc
    
    def __eq__(self, o) -> bool:
        if len(o.enc_ls) == len(self.enc_ls):
            return True
        return False
    
    def __gt__(self,o) -> bool:
        if len(o.enc_ls) < len(self.enc_ls):
            return True
        return False
    
    def __ge__(self,o) -> bool:
        if len(o.enc_ls) <= len(self.enc_ls):
            return True
        return False
    
    def __ne__(self,o) -> bool:
        if len(o.enc_ls) != len(self.enc_ls):
            return True
        return False
    
    def __lt__(self,o) -> bool:
        if len(o.enc_ls) > len(self.enc_ls):
            return True
        return False
    
    def __le__(self,o) -> bool:
        if len(o.enc_ls) >= len(self.enc_ls):
            return True
        return False
    
    def enc(self,s):
        t_enc = s
        for i in self.enc_ls:
            t_enc = i(t_enc,self.key)
        return t_enc
    
    def dec(self,s):
        t_dec = s
        for i in self.dec_ls:
            t_dec = i(t_dec,self.key)
        return t_dec

    def __str__(self):
        return '('.join([str(i).split(' ')[1] for i in self.enc_ls]) + f"(string)) -> Key Is {self.key}"

class Save:
    def __init__(self,file_name,**kwargs):
        self.file_name = file_name
        self.vars_list = kwargs
    
    def add_var(self,key,value):
        self.vars_list[key] = value
    
    def add_vars(self,**kwargs):
        self.vars_list.update(kwargs)
    
    def __call__(self):
        Pickler(open(self.file_name,"wb")).dump(self.vars_list)
    
    def save(self):
        Pickler(open(self.file_name,"wb")).dump(self.vars_list)

class Load:
    def __init__(self,file_name):
        self.file_name = file_name
        self.vars_list = Unpickler(open(self.file_name,"rb")).load()
    
    def vars(self):
        return self.vars_list
    
    def __call__(self,module):
        for i,j in self.vars_list.items():
            setattr(module, i, j)
    
    def load(self,module):
        for i,j in self.vars_list.items():
            setattr(module, i, j)

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

def b32_en(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b32encode(string).decode('utf-8')

def b32_de(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b32decode(string).decode('utf-8')

def b16_en(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b16encode(string).decode('utf-8')

def b16_de(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b16decode(string).decode('utf-8')

def b85_en(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b85encode(string).decode('utf-8')

def b85_de(string,k=""):
    if type(string) == str:
        string = bytes(string,encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b85decode(string).decode('utf-8')

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
            return Crypto([xor],[xor],key)
        elif alg.name == Algorithms.Base64.name:
            return Crypto([b64_en],[b64_de],key)
        elif alg.name == Algorithms.Cipher.name:
            return Crypto([cipher_en],[cipher_de],key)
        elif alg.name == Algorithms.Base16.name:
            return Crypto([b16_en],[b16_de],key)
        elif alg.name == Algorithms.Base32.name:
            return Crypto([b32_en],[b32_de],key)
        elif alg.name == Algorithms.Base85.name:
            return Crypto([b85_en],[b85_de],key)
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
            elif hasattr(i,'name') and i.name == Algorithms.Base16.name:
                ls_en.append(b16_en)
                ls_de.append(b16_de)
            elif hasattr(i,'name') and i.name == Algorithms.Base32.name:
                ls_en.append(b32_en)
                ls_de.append(b32_de)
            elif hasattr(i,'name') and i.name == Algorithms.Base85.name:
                ls_en.append(b85_en)
                ls_de.append(b85_de)
            else:
                raise AlgorithmError(f"Type {i} Is Not Supported. Just (Algorithms.Base64/Algorithms.XOR/Algorithms.Cypher) Is Supported.")
        return Crypto(ls_en,ls_de[::-1],key)
    else:
        raise AlgorithmError(f"This Type Of Algorithm Is Not Supported. Just enum.EnumMeta (Algorithms.Base64/...),list and set Are Supported.")
