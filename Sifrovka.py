import base64

MORSE = {
    'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',
    'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
    'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
    'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
    'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--',
    'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
    ',': '--..--', '?': '..--..', '!': '-.-.--', ' ': '/',

    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
}

ABC_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ABC_ENG = 'abcdefghijklmnopqrstuvwxyz'


def caesar_encrypt(text: str, shift: int) -> str:
    text = text.lower()
    result = []
    for char in text:
        if char in ABC_ENG:
            result.append(ABC_ENG[(ABC_ENG.index(char) + shift) % len(ABC_ENG)])
        elif char in ABC_RU:
            result.append(ABC_RU[(ABC_RU.index(char) + shift) % len(ABC_RU)])
        else:
            result.append(char)
    return ''.join(result)


def base64_encode(self, text: str) -> str:
    return base64.b64encode(text.lower().encode('utf-8')).decode('utf-8')


def xor_encrypt(self, text: str, key: str) -> str:
    text = text.lower()
    key = key.lower()
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))


def atbash_encrypt(text: str) -> str:
    text = text.lower()
    result = []
    for char in text:
        if char in ABC_ENG:
            result.append(ABC_ENG[len(ABC_ENG) - ABC_ENG.index(char) - 1])
        elif char in ABC_RU:
            result.append(ABC_RU[len(ABC_RU) - ABC_RU.index(char) - 1])
        else:
            result.append(char)
    return ''.join(result)


def rot13_encrypt(self, text: str) -> str:
    text = text.lower()
    result = []
    for char in text:
        if 'а' <= char <= 'я' or char == 'ё':
            if char == 'ё':
                base = ord('е')
            else:
                base = ord(char)
            result.append(chr((base - ord('а') + 13) % 33 + ord('а')))
        else:
            result.append(char)
    return ''.join(result)


def morse_encode(text: str) -> str:
    text = text.lower()
    return ' '.join(MORSE.get(char, char) for char in text)


def vigenere_encrypt(text, key):
    text = text.lower()
    key = key.lower()
    result = []
    key_index = 0
    for char in text:
        if char in ABC_RU:
            char_pos = ABC_RU.index(char)
            key_pos = ABC_RU.index(key[key_index % len(key)])
            encrypted_pos = (char_pos + key_pos) % len(ABC_RU)
            result.append(ABC_RU[encrypted_pos])
            key_index += 1
        elif char in ABC_ENG:
            char_pos = ABC_ENG.index(char)
            key_pos = ABC_ENG.index(key[key_index % len(key)])
            encrypted_pos = (char_pos + key_pos) % len(ABC_ENG)
            result.append(ABC_ENG[encrypted_pos])
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


encrypt_dict = {
    'morse': morse_encode,
    'caesar': caesar_encrypt,
    'atbash': atbash_encrypt
}
