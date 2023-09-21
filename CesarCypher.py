#/usr/bin/python3
from CommonEnglish import common_words

def caesar(ciphertext, shift):
    decrypted_text = ''
    for character in ciphertext:

        if character.isalpha():
            shifted_char_ascii_diff = ord(character.lower()) - ord('a') - shift
            shifted_char = chr((shifted_char_ascii_diff % 26) + ord('a'))

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