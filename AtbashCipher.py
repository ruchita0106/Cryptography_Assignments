def atbash_cipher(text):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr(ord('Z') - (ord(ch) - ord('A')))
        elif ch.islower():
            result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch 

    return result

text = input("Enter plain text for Atbash Cipher: ")

ciphertext = atbash_cipher(text)

print("\nAtbash Ciphertext:", ciphertext)