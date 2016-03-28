import hug

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
from rtfmapi.modules.crypto.types import *
import rtfmapi.modules.crypto.util

__all__=["Atbash","ADFGX","ADFGVX","SimpleSubstitution","Caesar","Affine","Enigma","Autokey","Beaufort",
         "Bifid","ColTrans","Gronsfeld","Foursquare","M209","PolybiusSquare","Playfair","Vigenere","Rot13","util",
         "Railfence","Porta","FracMorse"]



# ADFGX
@hug.post('/adfgx/encipher', output=hug.output_format.json)
def crypto_adfgx_encipher_api(key:type_key_square(25), keyword: 'The keyword, any word or phrase will do', msg: 'Message to be [de]ciphered'):
        """The ADFGX Cipher has a key consisting of a 5x5 key square and a word e.g. 'GERMAN'.
The algorithm is described here: http://www.practicalcryptography.com/ciphers/classical-era/adfgvx/
The key square consists of the letters A-Z with J omitted (25 characters total).""" 
        adfgx = ADFGX(key=key, keyword=keyword)
        return adfgx.encipher(msg)

@hug.post('/adfgx/decipher', output=hug.output_format.json)
def crypto_adfgx_decipher_api(key:type_key_square(25), keyword: 'The keyword, any word or phrase will do', msg: 'Message to be [de]ciphered'):
        """The ADFGX Cipher has a key consisting of a 5x5 key square and a word e.g. 'GERMAN'.
The algorithm is described here: http://www.practicalcryptography.com/ciphers/classical-era/adfgvx/
The key square consists of the letters A-Z with J omitted (25 characters total).""" 
        adfgx = ADFGX(key=key, keyword=keyword)
        return adfgx.decipher(msg)

# ADFGVX
@hug.post('/adfgvx/encipher', output=hug.output_format.json)
def crypto_adfgvx_encipher_api(key:type_key_square(36), keyword: 'The keyword, any word or phrase will do', msg: 'Message to be [de]ciphered'):
        """The ADFGVX Cipher has a key consisting of a 6x6 key square and a word e.g. 'GERMAN'.
The algorithm is described here: http://www.practicalcryptography.com/ciphers/classical-era/adfgvx/
The key square consists of the letters A-Z and the numbers 0-9 (36 characters total)"""
        adfgvx = ADFGVX(key=key, keyword=keyword)
        return adfgvx.encipher(msg)

@hug.post('/adfgvx/decipher', output=hug.output_format.json)
def crypto_adfgvx_decipher_api(key:type_key_square(36), keyword: 'The keyword, any word or phrase will do', msg: 'Message to be [de]ciphered'):
        """The ADFGVX Cipher has a key consisting of a 6x6 key square and a word e.g. 'GERMAN'.
The algorithm is described here: http://www.practicalcryptography.com/ciphers/classical-era/adfgvx/
The key square consists of the letters A-Z and the numbers 0-9 (36 characters total)"""
        adfgvx = ADFGVX(key=key, keyword=keyword)
        return adfgvx.decipher(msg)
        
# AFFINE
@hug.post('/affine/encipher', output=hug.output_format.json)
def crypto_affine_encipher_api(a:hug.types.one_of(['1','3','5','7','9','11','15','17','19','21','23','25']), b:hug.types.in_range(0,26), msg: 'Message to be [de]ciphered'):
        """The Affine Cipher has two components to the key, numbers *a* and *b*.
This cipher encrypts a letter according to the following equation::
    
        c = (a*p + b)%26
        
where c is the ciphertext letter, p the plaintext letter.
*b* is an integer 0-25, *a* is an integer that has an inverse (mod 26).
Allowable values for *a* are: 1,3,5,7,9,11,15,17,19,21,23,25 
For more info on the Affine cipher see http://www.practicalcryptography.com/ciphers/affine-cipher/""" 
        affine = Affine(a=int(a), b=int(b))
        return affine.encipher(msg)

@hug.post('/affine/decipher', output=hug.output_format.json)
def crypto_affine_decipher_api(a:hug.types.one_of(['1','3','5','7','9','11','15','17','19','21','23','25']), b:hug.types.in_range(0,26), msg: 'Message to be [de]ciphered'):
        """The Affine Cipher has two components to the key, numbers *a* and *b*.
This cipher encrypts a letter according to the following equation::
    
        c = (a*p + b)%26
        
where c is the ciphertext letter, p the plaintext letter.
*b* is an integer 0-25, *a* is an integer that has an inverse (mod 26).
Allowable values for *a* are: 1,3,5,7,9,11,15,17,19,21,23,25 
For more info on the Affine cipher see http://www.practicalcryptography.com/ciphers/affine-cipher/""" 
        affine = Affine(a=int(a), b=int(b))
        return affine.decipher(msg)

# ATBASH
@hug.post('/atbash/encipher', output=hug.output_format.json)
def crypto_atbash_encipher_api(msg: 'Message to be [de]ciphered'):
        """The Atbash Cipher has no key.
For more information see http://www.practicalcryptography.com/ciphers/atbash-cipher-cipher/."""
        atbash = Atbash()
        return atbash.encipher(msg)

@hug.post('/atbash/decipher', output=hug.output_format.json)
def crypto_atbash_decipher_api(msg: 'Message to be [de]ciphered'):
        """The Atbash Cipher has no key.
For more information see http://www.practicalcryptography.com/ciphers/atbash-cipher-cipher/."""
        atbash = Atbash()
        return atbash.decipher(msg)

# AUTOKEY
@hug.post('/autokey/encipher', output=hug.output_format.json)
def crypto_autokey_encipher_api(key:type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Autokey Cipher has a key consisting of a word e.g. 'FORTIFICATION'.
This cipher encrypts a letter according to the Vigenere tableau, the algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/classical-era/autokey/"""
        autokey = Autokey(key=key)
        return autokey.encipher(msg)

@hug.post('/autokey/decipher', output=hug.output_format.json)
def crypto_autokey_decipher_api(key:type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Autokey Cipher has a key consisting of a word e.g. 'FORTIFICATION'.
This cipher encrypts a letter according to the Vigenere tableau, the algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/classical-era/autokey/"""
        autokey = Autokey(key=key)
        return autokey.decipher(msg)

# BEAUFORT
@hug.post('/beaufort/encipher', output=hug.output_format.json)
def crypto_beaufort_encipher_api(key:type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Beaufort Cipher is similar to the Vigenere Cipher, and has a key consisting of a word e.g. 'FORTIFICATION'.
This cipher encrypts a letter according to the Vigenere tableau, the but uses a different algorithm to find the
ciphertext letter. The algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/beaufort-cipher/"""
        beaufort = Beaufort(key=key)
        return beaufort.encipher(msg)

@hug.post('/beaufort/decipher', output=hug.output_format.json)
def crypto_beaufort_decipher_api(key:type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Beaufort Cipher is similar to the Vigenere Cipher, and has a key consisting of a word e.g. 'FORTIFICATION'.
This cipher encrypts a letter according to the Vigenere tableau, the but uses a different algorithm to find the
ciphertext letter. The algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/beaufort-cipher/"""
        beaufort = Beaufort(key=key)
        return beaufort.decipher(msg)

# BIFID
@hug.post('/bifid/encipher', output=hug.output_format.json)
def crypto_bifid_encipher_api(key:type_key_square(25), period:hug.types.number, msg: 'Message to be [de]ciphered'):
        """The Bifid Cipher is a fractionating cipher, and has a key consisting of a 25 letter keysquare (with a letter removed e.g. 'J'), along with
a 'period', which is an integer.
For more information, the algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/bifid-cipher/"""
        bifid = Bifid(key=key, period=period)
        return bifid.encipher(msg)

@hug.post('/bifid/decipher', output=hug.output_format.json)
def crypto_bifid_decipher_api(key:type_key_square(25), period:hug.types.number, msg: 'Message to be [de]ciphered'):
        """The Bifid Cipher is a fractionating cipher, and has a key consisting of a 25 letter keysquare (with a letter removed e.g. 'J'), along with
a 'period', which is an integer.
For more information, the algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/bifid-cipher/"""
        bifid = Bifid(key=key, period=period)
        return bifid.decipher(msg)



# CAESAR
@hug.post('/caesar/encipher', output=hug.output_format.json)
def crypto_caesar_encipher_api(key:hug.types.in_range(1,26), msg: 'Message to be [de]ciphered'):
            """The Caesar Cipher has a key consisting of an integer 1-25.
This cipher encrypts a letter according to the following equation::

    c = (p + key)%26
    
where c is the ciphertext letter, p the plaintext letter.
For more details on the Caesar cipher, see http://www.practicalcryptography.com/ciphers/caesar-cipher/"""
            caesar = Caesar(key=key)
            return caesar.encipher(msg)

@hug.post('/caesar/decipher', output=hug.output_format.json)
def crypto_caesar_decipher_api(key:hug.types.in_range(1,26), msg: 'Message to be [de]ciphered'):
            """The Caesar Cipher has a key consisting of an integer 1-25.
This cipher encrypts a letter according to the following equation::

    c = (p + key)%26
    
where c is the ciphertext letter, p the plaintext letter.
For more details on the Caesar cipher, see http://www.practicalcryptography.com/ciphers/caesar-cipher/"""
            caesar = Caesar(key=key)
            return caesar.decipher(msg)


# COLTRANS
@hug.post('/coltrans/encipher', output=hug.output_format.json)
def crypto_coltrans_encipher_api(keyword: type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Columnar Transposition Cipher is a fractionating cipher, and has a key consisting of a word e.g. 'GERMAN'
For more information, the algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/columnar-transposition-cipher/"""
        coltrans = ColTrans(keyword=keyword)
        return coltrans.encipher(msg)

@hug.post('/coltrans/decipher', output=hug.output_format.json)
def crypto_coltrans_decipher_api(keyword: type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Columnar Transposition Cipher is a fractionating cipher, and has a key consisting of a word e.g. 'GERMAN'
For more information, the algorithm can be 
seen e.g. http://www.practicalcryptography.com/ciphers/columnar-transposition-cipher/"""
        coltrans = ColTrans(keyword=keyword)
        return coltrans.decipher(msg)


# DELASTELLE
@hug.post('/delastelle/encipher', output=hug.output_format.json)
def crypto_delastelle_encipher_api(key:type_key_cube, chars:type_char_set(3), msg: 'Message to be [de]ciphered'):
        """The Delastelle cipher is a simple substitution cipher that outputs 3 characters of ciphertext for each character of plaintext. It has a key consisting
of a 'key cube' 27 characters in length. This cipher is used as part of the Trifid cipher.
For a more detailed look at how it works see http://www.practicalcryptography.com/ciphers/trifid-cipher/."""
        delastelle = Delastelle(key=key, chars=chars)
        return delastelle.encipher(msg)

@hug.post('/delastelle/decipher', output=hug.output_format.json)
def crypto_delastelle_decipher_api(key:type_key_cube, chars:type_char_set(3), msg: 'Message to be [de]ciphered'):
        """The Delastelle cipher is a simple substitution cipher that outputs 3 characters of ciphertext for each character of plaintext. It has a key consisting
of a 'key cube' 27 characters in length. This cipher is used as part of the Trifid cipher.
For a more detailed look at how it works see http://www.practicalcryptography.com/ciphers/trifid-cipher/."""
        delastelle = Delastelle(key=key, chars=chars)
        return delastelle.decipher(msg)


# ENIGMA
@hug.post('/enigma/encipher', output=hug.output_format.json)
def crypto_enigma_encipher_api(settings:type_enigma_settings, rotors:type_enigma_rotors, reflector:type_enigma_reflector, ringstellung:type_enigma_ringstellung, steckers:type_enigma_steckers, msg: 'Message to be [de]ciphered'):
        """The Enigma M3 cipher"""
        enigma = Enigma(settings=settings, rotors=rotors, reflector=reflector, ringstellung=ringstellung, steckers=steckers)
        return enigma.encipher(msg)

@hug.post('/enigma/decipher', output=hug.output_format.json)
def crypto_enigma_decipher_api(settings:type_enigma_settings, rotors:type_enigma_rotors, reflector:type_enigma_reflector, ringstellung:type_enigma_ringstellung, steckers:type_enigma_steckers, msg: 'Message to be [de]ciphered'):
        """The Enigma M3 cipher"""
        enigma = Enigma(settings=settings, rotors=rotors, reflector=reflector, ringstellung=ringstellung, steckers=steckers)
        return enigma.decipher(msg)

# FOURSQUARE
@hug.post('/foursquare/encipher', output=hug.output_format.json)
def crypto_foursquare_encipher_api(key1:type_key_square(25, 'first'), key2:type_key_square(25,'second'), msg: 'Message to be [de]ciphered'):
        """The Foursquare Cipher enciphers pairs of characters, the key consists of 2 keysquares, each 25 characters in length.
More information about the algorithm can be 
found at http://www.practicalcryptography.com/ciphers/four-square-cipher/"""
        foursquare = Foursquare(key1=key1, key2=key2)
        return foursquare.encipher(msg)

@hug.post('/foursquare/decipher', output=hug.output_format.json)
def crypto_foursquare_decipher_api(key1:type_key_square(25,'first'), key2:type_key_square(25,'second'), msg: 'Message to be [de]ciphered'):
        """The Foursquare Cipher enciphers pairs of characters, the key consists of 2 keysquares, each 25 characters in length.
More information about the algorithm can be 
found at http://www.practicalcryptography.com/ciphers/four-square-cipher/"""
        foursquare = Foursquare(key=key1, key2=key2)
        return foursquare.decipher(msg)

# FRACMORSE
@hug.post('/fracmorse/encipher', output=hug.output_format.json)
def crypto_fracmorse_encipher_api(key:hug.types.length(26,27), msg: 'Message to be [de]ciphered'):
        """The Fractionated Morse Cipher has a 26 letter key, similar to that of a substitution cipher.
This cipher first converts the plaintext to morse code, then converts fixed-length chunks
of morse code back to ciphertext letters"""
        fracmorse = FracMorse(key=key)
        return fracmorse.encipher(msg)

@hug.post('/fracmorse/decipher', output=hug.output_format.json)
def crypto_fracmorse_decipher_api(key:hug.types.length(26,27), msg: 'Message to be [de]ciphered'):
        """The Fractionated Morse Cipher has a 26 letter key, similar to that of a substitution cipher.
This cipher first converts the plaintext to morse code, then converts fixed-length chunks
of morse code back to ciphertext letters"""
        fracmorse = FracMorse(key=key)
        return fracmorse.decipher(msg)

# GRONNSFELD
@hug.post('/gronsfeld/encipher', output=hug.output_format.json)
def crypto_gronsfeld_encipher_api(key:hug.types.multiple, msg: 'Message to be [de]ciphered'):
        """The Gronsfeld Cipher is similar to the Vigenere Cipher, and has a key consisting of a sequence of numbers 0-9 e.g. [4,9,2,0,2].
This cipher encrypts a letter according to the Vigenere tableau. More information about the algorithm can be 
found at http://www.practicalcryptography.com/ciphers/vigenere-gronsfeld-and-autokey-cipher/"""
        gronsfeld = Gronsfeld(key=key)
        return gronsfeld.encipher(msg)

@hug.post('/gronsfeld/decipher', output=hug.output_format.json)
def crypto_gronsfeld_decipher_api(key:hug.types.multiple, msg: 'Message to be [de]ciphered'):
        """The Gronsfeld Cipher is similar to the Vigenere Cipher, and has a key consisting of a sequence of numbers 0-9 e.g. [4,9,2,0,2].
This cipher encrypts a letter according to the Vigenere tableau. More information about the algorithm can be 
found at http://www.practicalcryptography.com/ciphers/vigenere-gronsfeld-and-autokey-cipher/"""
        gronsfeld = Gronsfeld(key=key)
        return gronsfeld.decipher(msg)


# M209
@hug.post('/m209/encipher', output=hug.output_format.json)
def crypto_m209_encipher_api(wheel_starts:type_m209_wheel_starts, w1s:type_m209_wheel(1,26), w2s:type_m209_wheel(2,25), w3s:type_m209_wheel(3,21), w4s:type_m209_wheel(4,21), w5s:type_m209_wheel(5,19), w6s:type_m209_wheel(6,17), lugpos:type_m209_lugpos, msg: 'Message to be [de]ciphered'):
        """The M209 cipher"""
        m209 = M209(wheel_starts=wheel_starts, w1s=w1s, w2s=w2s, w3s=w3s, w4s=w4s, w5s=w5s, w6s=w6s, lugpos=lugpos)
        return m209.encipher(msg)

@hug.post('/m209/decipher', output=hug.output_format.json)
def crypto_m209_decipher_api(wheel_starts:type_m209_wheel_starts, w1s:type_m209_wheel(1,26), w2s:type_m209_wheel(2,25), w3s:type_m209_wheel(3,21), w4s:type_m209_wheel(4,21), w5s:type_m209_wheel(5,19), w6s:type_m209_wheel(6,17), lugpos:type_m209_lugpos, msg: 'Message to be [de]ciphered'):
        """The M209 cipher"""
        m209 = M209(wheel_starts=wheel_starts, w1s=w1s, w2s=w2s, w3s=w3s, w4s=w4s, w5s=w5s, w6s=w6s, lugpos=lugpos)
        return m209.decipher(msg)



# PLAYFAIR
@hug.post('/playfair/encipher', output=hug.output_format.json)
def crypto_playfair_encipher_api(key:type_key_square(25), msg: 'Message to be [de]ciphered'):
        """The Playfair Cipher enciphers pairs of characters, the key consists of a keysquare 25 characters in length.
More information about the algorithm can be 
found at http://www.practicalcryptography.com/ciphers/playfair-cipher/"""
        playfair = Playfair(key=key)
        return playfair.encipher(msg)

@hug.post('/playfair/decipher', output=hug.output_format.json)
def crypto_playfair_decipher_api(key:type_key_square(25), msg: 'Message to be [de]ciphered'):
        """The Playfair Cipher enciphers pairs of characters, the key consists of a keysquare 25 characters in length.
More information about the algorithm can be 
found at http://www.practicalcryptography.com/ciphers/playfair-cipher/"""
        playfair = Playfair(key=key)
        return playfair.decipher(msg)


# POLYBIUS
@hug.post('/polybius/encipher', output=hug.output_format.json)
def crypto_polybius_encipher_api(key: 'The keysquare, each row one after the other. The key must by size^2 characters in length', size:type_key_square_size, chars:'the set of characters to use. By default ABCDE are used, this parameter should have the same length as size', msg: 'Message to be [de]ciphered'):
    """The Polybius square is a simple substitution cipher that outputs 2 characters of ciphertext for each character of plaintext. It has a key consisting
which depends on 'size'. By default 'size' is 5, and the key is 25 letters (5^2). For a size of 6 a 36 letter key required etc.
For a more detailed look at how it works see http://www.practicalcryptography.com/ciphers pycipher.polybius-square-cipher/"""
    if len(key) == size**2 and len(chars) == size:
        polybius = PolybiusSquare(key=key, size=size, chars=chars)
        return polybius.encipher(msg)
    else:
        return 'Invalid parameters'

@hug.post('/polybius/decipher', output=hug.output_format.json)
def crypto_polybius_decipher_api(key: 'The keysquare, each row one after the other. The key must by size^2 characters in length', size:type_key_square_size, chars:'the set of characters to use. By default ABCDE are used, this parameter should have the same length as size', msg: 'Message to be [de]ciphered'):
    """The Polybius square is a simple substitution cipher that outputs 2 characters of ciphertext for each character of plaintext. It has a key consisting
which depends on 'size'. By default 'size' is 5, and the key is 25 letters (5^2). For a size of 6 a 36 letter key required etc.
For a more detailed look at how it works see http://www.practicalcryptography.com/ciphers pycipher.polybius-square-cipher/"""
    if len(key) == size**2 and len(chars) == size:
        polybius = PolybiusSquare(key=key, size=size, chars=chars)
        return polybius.decipher(msg)
    else:
        return 'Invalid parameters'


# PORTA
@hug.post('/porta/encipher', output=hug.output_format.json)
def crypto_porta_encipher_api(key:type_alphabetical_key, keyword, msg: 'Message to be [de]ciphered'):
        """The Porta Cipher is a polyalphabetic substitution cipher, and has a key consisting of a word e.g. 'FORTIFICATION'."""
        porta = Porta(key=key, keyword=keyword)
        return porta.encipher(msg)

@hug.post('/porta/decipher', output=hug.output_format.json)
def crypto_porta_decipher_api(key:type_alphabetical_key, keyword, msg: 'Message to be [de]ciphered'):
        """The Porta Cipher is a polyalphabetic substitution cipher, and has a key consisting of a word e.g. 'FORTIFICATION'."""
        porta = Porta(key=key, keyword=keyword)
        return porta.decipher(msg)

# RAILFENCE
@hug.post('/railfence/encipher', output=hug.output_format.json)
def crypto_railfence_encipher_api(key:hug.types.greater_than(0), msg: 'Message to be [de]ciphered'):
        """The Railfence Cipher has a single number that forms the key.
For more info on the Railfence cipher see http://www.practicalcryptography.com/ciphers/rail-fence-cipher/"""
        railfence = Railfence(key=key)
        return railfence.encipher(msg)

@hug.post('/railfence/decipher', output=hug.output_format.json)
def crypto_railfence_decipher_api(key:hug.types.greater_than(0), msg: 'Message to be [de]ciphered'):
        """The Railfence Cipher has a single number that forms the key.
For more info on the Railfence cipher see http://www.practicalcryptography.com/ciphers/rail-fence-cipher/"""
        railfence = Railfence(key=key)
        return railfence.decipher(msg)


# ROT13
@hug.post('/rot13/encipher', output=hug.output_format.json)
def crypto_rot13_encipher_api(msg: 'Message to be [de]ciphered'):
        """The Rot13 Cipher has no key, it is commonly used just to hide text.
This cipher encrypts a letter according to the following equation::

    c = (p + 13)%26
    
where c is the ciphertext letter, p the plaintext letter. This is equivalent to the Caesar cipher with a key of 13.
For more details on the rot13 cipher, see http://www.practicalcryptography.com/ciphers/rot13-cipher/"""
        rot13 = Rot13()
        return rot13.encipher(msg)

@hug.post('/rot13/decipher', output=hug.output_format.json)
def crypto_rot13_decipher_api(msg: 'Message to be [de]ciphered'):
        """The Rot13 Cipher has no key, it is commonly used just to hide text.
This cipher encrypts a letter according to the following equation::

    c = (p + 13)%26
    
where c is the ciphertext letter, p the plaintext letter. This is equivalent to the Caesar cipher with a key of 13.
For more details on the rot13 cipher, see http://www.practicalcryptography.com/ciphers/rot13-cipher/"""
        rot13 = Rot13()
        return rot13.decipher(msg)


# SIMPLESUBSTITUTION
@hug.post('/simplesubstitution/encipher', output=hug.output_format.json)
def crypto_simplesubstitution_encipher_api(key:type_key_alphabet_permutation, msg: 'Message to be [de]ciphered'):
        """The Simple Substitution Cipher has a key consisting of the letters A-Z jumbled up.
e.g. 'AJPCZWRLFBDKOTYUQGENHXMIVS'
This cipher encrypts a letter according to the following equation::
    plaintext =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ciphertext = AJPCZWRLFBDKOTYUQGENHXMIVS
To convert a plaintext letter into ciphertext, read along the plaintext row until the desired
letter is found, then substitute it with the letter below it. For more information see http://www.practicalcryptography.com/ciphers/simple-substitution-cipher/"""
        simplesubstitution = SimpleSubstitution(key=key)
        return simplesubstitution.encipher(msg)

@hug.post('/simplesubstitution/decipher', output=hug.output_format.json)
def crypto_simplesubstitution_decipher_api(key:type_key_alphabet_permutation, msg: 'Message to be [de]ciphered'):
        """The Simple Substitution Cipher has a key consisting of the letters A-Z jumbled up.
e.g. 'AJPCZWRLFBDKOTYUQGENHXMIVS'
This cipher encrypts a letter according to the following equation::
    plaintext =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ciphertext = AJPCZWRLFBDKOTYUQGENHXMIVS
To convert a plaintext letter into ciphertext, read along the plaintext row until the desired
letter is found, then substitute it with the letter below it. For more information see http://www.practicalcryptography.com/ciphers/simple-substitution-cipher/"""
        simplesubstitution = SimpleSubstitution(key=key)
        return simplesubstitution.decipher(msg)

# VIGENERE
@hug.post('/vigenere/encipher', output=hug.output_format.json)
def crypto_vigenere_encipher_api(key:type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Vigenere Cipher has a key consisting of a word e.g. 'FORTIFICATION'.
This cipher encrypts a letter according to the Vigenere tableau, the algorithm can be 
seen e.g. http://practicalcryptography.com/ciphers/vigenere-gronsfeld-and-autokey-cipher/"""
        vigenere = ADFGVX(key=key)
        return vigenere.encipher(msg)

@hug.post('/vigenere/decipher', output=hug.output_format.json)
def crypto_vigenere_decipher_api(key:type_alphabetical_key, msg: 'Message to be [de]ciphered'):
        """The Vigenere Cipher has a key consisting of a word e.g. 'FORTIFICATION'.
This cipher encrypts a letter according to the Vigenere tableau, the algorithm can be 
seen e.g. http://practicalcryptography.com/ciphers/vigenere-gronsfeld-and-autokey-cipher/"""
        vigenere = Vigenere(key=key)
        return vigenere.decipher(msg)
