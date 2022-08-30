import base64
import string
from exceptions import *
from enums import Algorithms
from pickle import Unpickler, Pickler


class Crypto:

    """
Crypto Class Is Made For Do Encryption And Decryption More Coder Friendly :)
    """

    def __init__(self, enc_ls, dec_ls, key):
        self.enc_ls = enc_ls
        self.dec_ls = dec_ls
        self.key = key

    def __call__(self, s):
        t_enc = s
        for i in self.enc_ls:
            t_enc = i(t_enc, self.key)
        return t_enc

    def __eq__(self, o) -> bool:
        if len(o.enc_ls) == len(self.enc_ls):
            return True
        return False

    def __gt__(self, o) -> bool:
        if len(o.enc_ls) < len(self.enc_ls):
            return True
        return False

    def __ge__(self, o) -> bool:
        if len(o.enc_ls) <= len(self.enc_ls):
            return True
        return False

    def __ne__(self, o) -> bool:
        if len(o.enc_ls) != len(self.enc_ls):
            return True
        return False

    def __lt__(self, o) -> bool:
        if len(o.enc_ls) > len(self.enc_ls):
            return True
        return False

    def __le__(self, o) -> bool:
        if len(o.enc_ls) >= len(self.enc_ls):
            return True
        return False

    def enc(self, s):
        t_enc = s
        for i in self.enc_ls:
            t_enc = i(t_enc, self.key)
        return t_enc

    def dec(self, s):
        t_dec = s
        for i in self.dec_ls:
            t_dec = i(t_dec, self.key)
        return t_dec

    def __str__(self):
        return '('.join([str(i).split(' ')[1] for i in self.enc_ls]) + f"(string)) -> Key Is {self.key}"


class Save:
    """
A Class To Save Some Variables With Some Simple Encryption. Example : 

```
Save("file.txt",name="test",family="123",...)()

# Or 
handler = Save("file.txt")
handler.add_var("name","Arshia")
handler.add_vars({"nickname":"MrMegaExpert","age":21})
handler.save() # Or handler()

# Or 
handler = Save("file.txt")
handler["name"] = "Arshia"
handler.save() # Or handler()
```
    """

    def __init__(self, file_name, **kwargs):
        self.file_name = file_name
        self.vars_list = kwargs

    def add_var(self, key, value):
        self.vars_list[key] = value

    def add_vars(self, **kwargs):
        self.vars_list.update(kwargs)

    def __setitem__(self, key, value):
        self.vars_list[key] = value

    def __getitem__(self, key):
        return self.vars_list[key]

    def __call__(self):
        Pickler(open(self.file_name, "wb")).dump(self.vars_list)

    def save(self):
        Pickler(open(self.file_name, "wb")).dump(self.vars_list)


class Load:
    """
A Class To Load Saved Variables. Example : 

```
def test():
    print(name)

Load("file.txt")(test)

# Or 
handler = Load("file.txt")
print(handler.vars) # All Variables As Dictionary

# Or 
Load("file.txt")()
print(name) # If You Saved name It Will Be Shown :)
```

    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.vars_list = Unpickler(open(self.file_name, "rb")).load()

    def vars(self):
        return self.vars_list

    def __call__(self, module=None):
        for i, j in self.vars_list.items():
            if not module:
                globals()[i] = j
            else:
                setattr(module, i, j)

    def load(self, module=None):
        for i, j in self.vars_list.items():
            if not module:
                globals()[i] = j
            else:
                setattr(module, i, j)


def _xor(string, key=0):
    """
xor function. got string And key At The End; It Will Encrypt/Decrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
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


def _b64_en(string, k=""):
    """
base64 Encoder function. got string And key (Fake) At The End; It Will Encrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b64encode(string).decode('utf-8')


def _b64_de(string, k=""):
    """
base64 Decoder function. got string And key (Fake) At The End; It Will Decrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b64decode(string).decode('utf-8')


def _b32_en(string, k=""):
    """
base32 Encoder function. got string And key (Fake) At The End; It Will Encrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b32encode(string).decode('utf-8')


def _b32_de(string, k=""):
    """
base32 Decoder function. got string And key (Fake) At The End; It Will Decrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b32decode(string).decode('utf-8')


def _b16_en(string, k=""):
    """
base16 Encoder function. got string And key (Fake) At The End; It Will Encrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b16encode(string).decode('utf-8')


def _b16_de(string, k=""):
    """
base16 Decoder function. got string And key (Fake) At The End; It Will Decrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b16decode(string).decode('utf-8')


def _b85_en(string, k=""):
    """
base85 Encoder function. got string And key (Fake) At The End; It Will Encrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b85encode(string).decode('utf-8')


def _b85_de(string, k=""):
    """
base85 Decoder function. got string And key (Fake) At The End; It Will Decrypt Your Data.
    """
    if type(string) == str:
        string = bytes(string, encoding='utf-8')
    elif type(string) == bytes:
        pass
    else:
        raise TypeError("Type Should Be 'str' Or 'bytes'.")
    return base64.b85decode(string).decode('utf-8')


def _cipher_en(s, key=1):
    """
Cipher Encoder function. got string And key At The End; It Will Encrypt Your,Data.
    """
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


def _cipher_de(s, key=1):
    """
Cipher Decoder function. got string And key At The End; It Will Decrypt Your Data.
    """
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


def _rot13(string):
    """
ROT13 function. It Will Encrypt Your Data In This Algorythm.
    """
    slow = string.ascii_lowercase
    sup = string.ascii_uppercase

    ans = ""

    for i in string:
        if i in string.ascii_lowercase:
            ans += slow[(slow.index(i) + 13) % 26]
        elif i in string.ascii_uppercase:
            ans += sup[(sup.index(i) + 13) % 26]
        else:
            ans += i

    return ans


def _unrot13(string):
    """
ROT13 Decoder function. It Will Decrypt Your Data In This Algorythm.
    """
    slow = string.ascii_lowercase
    sup = string.ascii_uppercase

    ans = ""

    for i in string:
        if i in string.ascii_lowercase:
            ans += slow[(slow.index(i) - 13) % 26]
        elif i in string.ascii_uppercase:
            ans += sup[(sup.index(i) - 13) % 26]
        else:
            ans += i

    return ans


def make_enc(alg, key=b""):
    """
make_enc Function Will Make You An instance Of Crypto Class That Contains A
Chain Of Encryption Algorithm. In Fact You Are Free To Use Just One Or More.
Args/Kwargs :
* alg     ->    The Algorithm That Can Be Like Algorithms.XOR Or Like 
                [Algorithms.XOR,Algorithms.Base64]

* key     ->    The Target Key That You Want To Use In Encryption Process.

Example :

```a = make_enc([Algorithms.XOR,Algorithms.Base64],10)
a.enc("Hello")    # Encrypt "Hello" Equals "Qm9mZmU="
a.dec("Qm9mZmU=") # Decrypt "Qm9mZmU" Equals "Hello"```
    """
    if str(type(alg)) == "<enum 'Algorithms'>":
        if alg.name == Algorithms.XOR.name:
            return Crypto([_xor], [_xor], key)
        elif alg.name == Algorithms.ROT13.name:
            return Crypto([_rot13], [_unrot13], key)
        elif alg.name == Algorithms.Base64.name:
            return Crypto([_b64_en], [_b64_de], key)
        elif alg.name == Algorithms.Cipher.name:
            return Crypto([_cipher_en], [_cipher_de], key)
        elif alg.name == Algorithms.Base16.name:
            return Crypto([_b16_en], [_b16_de], key)
        elif alg.name == Algorithms.Base32.name:
            return Crypto([_b32_en], [_b32_de], key)
        elif alg.name == Algorithms.Base85.name:
            return Crypto([_b85_en], [_b85_de], key)
        else:
            raise AlgorithmError(
                f"This Algorithm Is Not Available. We Will Be Happy If You Help Us To Make It :)\nGithub : https://github.com/Arshiatmi/Pysha")
    elif type(alg) == list or type(alg) == set or type(alg) == tuple:
        ls_en = []
        ls_de = []
        for i in alg:
            if hasattr(i, 'name') and i.name == Algorithms.XOR.name:
                ls_en.append(_xor)
                ls_de.append(_xor)
            elif hasattr(i, 'name') and i.name == Algorithms.Base64.name:
                ls_en.append(_b64_en)
                ls_de.append(_b64_de)
            elif hasattr(i, 'name') and i.name == Algorithms.Cipher.name:
                ls_en.append(_cipher_en)
                ls_de.append(_cipher_de)
            elif hasattr(i, 'name') and i.name == Algorithms.Base16.name:
                ls_en.append(_b16_en)
                ls_de.append(_b16_de)
            elif hasattr(i, 'name') and i.name == Algorithms.Base32.name:
                ls_en.append(_b32_en)
                ls_de.append(_b32_de)
            elif hasattr(i, 'name') and i.name == Algorithms.Base85.name:
                ls_en.append(_b85_en)
                ls_de.append(_b85_de)
            elif hasattr(i, 'name') and i.name == Algorithms.ROT13.name:
                ls_en.append(_rot13)
                ls_de.append(_unrot13)
            else:
                raise AlgorithmError(
                    f"Type {i} Is Not Supported. Just (Algorithms.Base64/Algorithms.XOR/Algorithms.Cypher) Is Supported.")
        return Crypto(ls_en, ls_de[::-1], key)
    else:
        raise AlgorithmError(
            f"This Type Of Algorithm Is Not Supported. Just enum.EnumMeta (Algorithms.Base64/...),list and set Are Supported.")
