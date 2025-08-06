import string
def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    seen = set()
    cipher_alphabet = ""

    for ch in keyword:
        if ch.isalpha() and ch not in seen:
            cipher_alphabet += ch
            seen.add(ch)

    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if ch not in seen:
            cipher_alphabet += ch
    return cipher_alphabet

def keyword_encrypt(plaintext, keyword):
    cipher_alphabet = generate_cipher_alphabet(keyword)
    result = ""

    for ch in plaintext:
        if ch.isupper():
            index = ord(ch) - ord('A')
            result += cipher_alphabet[index]
        elif ch.islower():
            index = ord(ch) - ord('a')
            result += cipher_alphabet[index].lower()
        else:
            result += ch
    return result

plaintext = input("Enter the Plaintext: ")
keyword = input("Enter the Keyword: ")

encrypted = keyword_encrypt(plaintext, keyword)
print("Encrypted text(cipher text): ", encrypted)
