from .functions import *
import getpass

# Authentication Class
#  Mode 0 -> Not Show Password
#  Mode 1 -> Star Password
#  Mode 2 -> Normal Input
class Auth:
    def __init__(self,first_prompt="Enter Your Username : ",second_prompt="Enter Your Password : ",mode=0,mask='*'):
        self.first_prompt = first_prompt
        self.second_prompt = second_prompt
        self.mode = mode
        self.mask = mask
    
    """
    Argumets : 
        c           ->  If Its True colorize Function Will Be Executed On Prompts.
        mask_color  ->  Set Color For Password Mask.
        inp_color   ->  Set Color For Username Mask.
        mask        ->  Set Mask Character.
    """
    def auth(self,c=True,mask_color=fore["reset"],inp_color=fore["reset"],mask='*'):
        tar = self.mask
        if mask != '*':
            tar = mask
        if len(tar.strip()):pass
        if c:
            ans = []
            if self.mode == 0:
                uname = colorprompt(colorize(self.first_prompt),char_color=inp_color)
                pwd = getpass.getpass(colorize(self.second_prompt))
                ans.append(uname)
                ans.append(pwd)
            elif self.mode == 1:
                uname = colorprompt(colorize(self.first_prompt),char_color=inp_color)
                pwd = passprompt(colorize(self.second_prompt),mask_color=mask_color,mask=mask)
                ans.append(uname)
                ans.append(pwd)
            elif self.mode == 2:
                uname = colorprompt(colorize(self.first_prompt),char_color=inp_color)
                pwd = input(prompt=colorize(self.second_prompt))
                ans.append(uname)
                ans.append(pwd)
            else:
                raise ModeError(f"Mode {self.mode} Is Not Available For Authentication. Just 0,1,2.")
            return ans
        else:
            ans = []
            if self.mode == 0:
                uname = colorprompt((self.first_prompt),char_color=inp_color)
                pwd = getpass.getpass((self.second_prompt))
                ans.append(uname)
                ans.append(pwd)
            elif self.mode == 1:
                uname = colorprompt((self.first_prompt),char_color=inp_color)
                pwd = passprompt(prompt=(self.second_prompt),mask=mask_color + tar + fore["reset"])
                ans.append(uname)
                ans.append(pwd)
            elif self.mode == 2:
                uname = colorprompt((self.first_prompt),char_color=inp_color)
                pwd = colorprompt((self.second_prompt),char_color=inp_color)
                ans.append(uname)
                ans.append(pwd)
            else:
                raise ModeError(f"Mode {self.mode} Is Not Available For Authentication. Just 0,1,2.")
            return ans