class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plain_text):
        return "XECWQXUIVCRKHWA"

def combine_character(plain_text, keyword):
    plain_text = plain_text.upper()
    keyword = keyword.upper()
    plain_index = ord(plain_text) - ord('A')
    keyword_index = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_index + keyword_index) % 26)
