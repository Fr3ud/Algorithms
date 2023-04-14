from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)

    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR

    return encrypted, dummy

def decrypt(encrypted: int, dummy: int) -> str:
    decrypted: int = encrypted ^ dummy # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")

    return temp.decode()


if __name__ == "__main__":
    encrypted, dummy = encrypt("Hello World!")
    result: str = decrypt(encrypted, dummy)

    print(result)
