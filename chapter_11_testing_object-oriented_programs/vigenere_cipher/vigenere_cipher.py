class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def _code(self, text, combine_func):
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    def encode(self, plain_text):
        return self._code(plain_text, combine_character)

    def decode(self, cipher_text):
        return self._code(cipher_text, separate_character)

    def extend_keyword(self, number):
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

def combine_character(plain_text, keyword):
    plain_text = plain_text.upper()
    keyword = keyword.upper()
    plain_index = ord(plain_text) - ord('A')
    keyword_index = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_index + keyword_index) % 26)

def separate_character(cypher, keyword):
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_index = ord(cypher) - ord('A')
    keyword_index = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_index - keyword_index) % 26)
