from rtfmapi.modules.crypto.adfgx import ADFGX 
from rtfmapi.modules.crypto.adfgvx import ADFGVX 
from rtfmapi.modules.crypto.simplesubstitution import SimpleSubstitution
from rtfmapi.modules.crypto.caesar import Caesar 
from rtfmapi.modules.crypto.affine import Affine
from rtfmapi.modules.crypto.enigma import Enigma 
from rtfmapi.modules.crypto.autokey import Autokey 
from rtfmapi.modules.crypto.beaufort import Beaufort 
from rtfmapi.modules.crypto.bifid import Bifid as Bifid
from rtfmapi.modules.crypto.columnartransposition import ColTrans 
from rtfmapi.modules.crypto.gronsfeld import Gronsfeld 
from rtfmapi.modules.crypto.foursquare import Foursquare 
from rtfmapi.modules.crypto.m209 import M209 as M209
from rtfmapi.modules.crypto.polybius import PolybiusSquare 
from rtfmapi.modules.crypto.playfair import Playfair 
from rtfmapi.modules.crypto.vigenere import Vigenere 
from rtfmapi.modules.crypto.rot13 import Rot13
from rtfmapi.modules.crypto.atbash import Atbash
from rtfmapi.modules.crypto.railfence import Railfence
from rtfmapi.modules.crypto.porta import Porta
from rtfmapi.modules.crypto.fracmorse import FracMorse
import rtfmapi.modules.crypto.util

__all__=["Atbash","ADFGX","ADFGVX","SimpleSubstitution","Caesar","Affine","Enigma","Autokey","Beaufort",
         "Bifid","ColTrans","Gronsfeld","Foursquare","M209","PolybiusSquare","Playfair","Vigenere","Rot13","util",
         "Railfence","Porta","FracMorse"]


# ADFGX
@hug.post('/adfgx/encipher', output=hug.output_format.json)
def crypto_adfgx_encipher_api(key, keyword, msg):
        adfgx = ADFGX(key=key, keyword=keyword)
        return adfgx.encipher(msg)

@hug.post('/adfgx/decipher', output=hug.output_format.json)
def crypto_adfgx_encipher_api(key, keyword, msg):
        adfgx = ADFGX(key=key, keyword=keyword)
        return adfgx.decipher(msg)

# ADFGVX
@hug.post('/adfgvx/encipher', output=hug.output_format.json)
def crypto_adfgvx_encipher_api(key, keyword, msg):
        adfgvx = ADFGVX(key=key, keyword=keyword)
        return adfgvx.encipher(msg)

@hug.post('/adfgvx/decipher', output=hug.output_format.json)
def crypto_adfgvx_encipher_api(key, keyword, msg):
        adfgvx = ADFGVX(key=key, keyword=keyword)
        return adfgvx.decipher(msg)
        
#AFFINE
@hug.post('/affine/encipher', output=hug.output_format.json)
def crypto_affine_encipher_api(a:int, b:int, msg):
        affine = Affine(a=a, b=b)
        return affine.encipher(msg)

@hug.post('/affine/decipher', output=hug.output_format.json)
def crypto_affine_encipher_api(a:int, b:int, msg):
        affine = Affine(a=a, b=b)
        return affine.decipher(msg)

#ATBASH
@hug.post('/atbash/encipher', output=hug.output_format.json)
def crypto_atbash_encipher_api(msg):
        atbash = Atbash()
        return atbash.encipher(msg)

@hug.post('/atbash/decipher', output=hug.output_format.json)
def crypto_atbash_encipher_api(msg):
        atbash = Atbash()
        return atbash.decipher(msg)

#AUTOKEY
@hug.post('/autokey/encipher', output=hug.output_format.json)
def crypto_autokey_encipher_api(key, msg):
        autokey = Autokey(key=key)
        return autokey.encipher(msg)

@hug.post('/autokey/decipher', output=hug.output_format.json)
def crypto_autokey_encipher_api(key, msg):
        autokey = Autokey(key=key)
        return autokey.decipher(msg)
