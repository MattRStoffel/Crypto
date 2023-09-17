#/usr/bin/python3
from CommonEnglish import common_words

def caesar(ciphertext, shift):
    decrypted_text = ''
    for character in ciphertext:
        if character.isalpha():
            shifted_char = chr(((ord(character.lower()) - ord('a') - shift) % 26) + ord('a'))
            if character.isupper():
                decrypted_text += shifted_char.upper()
            else:
                decrypted_text += shifted_char
        else:
            decrypted_text += character
    return decrypted_text

def decrypt_cesar(ciphertext):
    outcomes = {}
    for shift in range(26):
        decrypted_text = caesar(ciphertext, shift)
        word_list = decrypted_text.split()
        valid_word_count = sum(1 for word in word_list if word.lower() in common_words)
        outcomes[decrypted_text] = valid_word_count

    return max(outcomes, key=outcomes.get)


input_text = """

eky znk sgzn vgxz, o joj ngvvkt zu lotj xkyuaxiky ut yusk zevoigr zuury zngz sgznksgzoiogty gtj ngiqkxy groqk igt ayk zu gtgrefk ktixevzout.

znoy oy g ykde xkyuaxik
nzzv://vxgizoigrixevzumxgvne.ius/ixevzgtgreyoy/
oz vxubojky g ruz ul otluxsgzout ut nuc eua cuarj mu ghuaz gtgreyotm jollkxktz iovnkxy

O qtuc znkxk'y g ruz suxk zu oz, yu nkxk gxk cgee suxk xkyuaxiky eua igt ayk
nzzvy://ccc.ixevzuvgry.ius/ nzzvy://ixevzungiq.uxm/

Znkyk gxk murj yzgtjgxj lux izly (gvvgxktzre) /\

Lux znk gizagr sgzn xkwaoxkj ... 👀👀👀👀👀👀👀👀
Eua'rr tkkj tashkx znkuxe, iushotgzuxoiy, grr zngz pgff zngz tu utk ngy znk zosk zu sgyzkx haz ol euaxk muotm grr znk cge eua sge gy ckrr atruiq znk yqkrkzut qke
"""

print(decrypt_cesar(input_text))

