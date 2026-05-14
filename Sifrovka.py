import base64


class Encrypt:
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

    @classmethod
    def caesar_encrypt(self, text: str, shift: int) -> str:
        text = text.lower()
        result = []
        for char in text:
            if char in self.ABC_ENG:
                result.append(self.ABC_ENG[(self.ABC_ENG.index(char) + shift) % len(self.ABC_ENG)])
            elif char in self.ABC_RU:
                result.append(self.ABC_RU[(self.ABC_RU.index(char) + shift) % len(self.ABC_RU)])
            else:
                result.append(char)
        return ''.join(result)

    def base64_encode(self, text: str) -> str:
        return base64.b64encode(text.lower().encode('utf-8')).decode('utf-8')

    def morse_encode(self, text: str) -> str:
        text = text.lower()
        return ' '.join(self.MORSE.get(char, char) for char in text)

    def xor_encrypt(self, text: str, key: str) -> str:
        text = text.lower()
        key = key.lower()
        key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
        return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))

    def atbash_encrypt(self, text: str) -> str:
        text = text.lower()
        result = []
        for char in text:
            if char in self.ABC_ENG:
                result.append(self.ABC_ENG[len(self.ABC_ENG) - self.ABC_ENG.index(char) - 1])
            elif char in self.ABC_RU:
                result.append(self.ABC_RU[len(self.ABC_RU) - self.ABC_RU.index(char) - 1])
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

    encrypt_dict = {
        'caesar': caesar_encrypt,
        'morse': morse_encode
    }
