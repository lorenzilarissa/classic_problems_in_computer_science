

# put the data in order

from secrets import token_bytes
from typing import Tuple 

def random_key(lenght: int) -> int:         # generates aleatory lenght bytes
    tb: bytes = token_bytes(lenght)         # convert the bytes into a string of bits and return it
    return int.from_bytes(tb, 'big')        # from_bytes convert bytes into int

# unbreakable encryption

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, 'big')
    encrypted: int = original_key ^ dummy   # XOR
    return dummy, encrypted

# decrypting

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2            #XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')      # rounding up
    return temp.decode()

# results

if __name__ == '__main__':
    key1, key2 = encrypt('One Time Pad!')
    result: str = decrypt(key1, key2)
    print(result)


