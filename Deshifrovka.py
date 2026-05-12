import base64


class CipherSuite:
    MORSE = {
        'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.',
        'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
        'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
        'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
        'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--',
        'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
        ',': '--..--', '?': '..--..', '!': '-.-.--', ' ': '/'
    }
    MORSE_REVERSE = {v: k for k, v in MORSE.items()}

    def caesar_decrypt(self, text: str, shift: int) -> str:
        text = text.lower()
        result = []
        for char in text:
            if 'а' <= char <= 'я' or char == 'ё':
                if char == 'ё':
                    base = ord('е')
                else:
                    base = ord(char)
                result.append(chr((base - ord('а') - shift) % 33 + ord('а')))
            else:
                result.append(char)
        return ''.join(result)

    def base64_decode(self, text: str) -> str:
        return base64.b64decode(text.encode('utf-8')).decode('utf-8').lower()

    def morse_decode(self, text: str) -> str:
        result = []
        for code in text.split(' '):
            if code in self.MORSE_REVERSE:
                result.append(self.MORSE_REVERSE[code])
            else:
                result.append(code)
        return ''.join(result).lower()

    def xor_decrypt(self, text: str, key: str) -> str:
        text = text.lower()
        key = key.lower()
        key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
        return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key)).lower()

    def atbash_decrypt(self, text: str) -> str:
        text = text.lower()
        result = []
        for char in text:
            if 'а' <= char <= 'я':
                result.append(chr(ord('я') - (ord(char) - ord('а'))))
            elif char == 'ё':
                result.append('ъ')
            else:
                result.append(char)
        return ''.join(result)

    def rot13_decrypt(self, text: str) -> str:
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
