import numpy as np

def to_nums(text):
    return [ord(c) - 65 for c in text]

def to_text(nums):
    return ''.join(chr(n % 26 + 65) for n in nums)

def encrypt(msg, key):
    msg = msg.upper().replace(" ", "")
    if len(msg) % 2: msg += 'X'
    result = ''
    for i in range(0, len(msg), 2):
        block = to_nums(msg[i:i+2])
        enc = np.dot(key, block) % 26
        result += to_text(enc)
    return result

try:
    msg = input("Enter plaintext: ")
    k = list(map(int, input("Enter 4 numbers for 2x2 key matrix: ").split()))
    
    if len(k) != 4:
        raise ValueError("You must enter exactly 4 integers.")
    
    key = np.array(k).reshape(2, 2)

    print("Encrypted:", encrypt(msg, key))

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Unexpected Error:", e)