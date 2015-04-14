from vigenere_cipher import VigenereCipher
from vigenere_cipher import combine_character
from vigenere_cipher import separate_character

def pytest_funcarg__valid_cipher(request):
    return VigenereCipher("TRAIN")

def test_encode(valid_cipher):
    assert valid_cipher.encode("ENCODEDINPYTHON") == "XECWQXUIVCRKHWA"

def test_encode_character(valid_cipher):
    assert valid_cipher.encode("E") == "X"

def test_encode_spaces(valid_cipher):
    assert valid_cipher.encode("ENCODED IN PYTHON") == "XECWQXUIVCRKHWA"

def test_encode_lowercase(valid_cipher):
    cipher = VigenereCipher("TRain")
    assert cipher.encode("encoded in Python") == "XECWQXUIVCRKHWA"

def test_combine_character():
    assert combine_character("E", "T") == "X"
    assert combine_character("N", "R") == "E"

def test_extend_keyword_to_length_15(valid_cipher):
    assert valid_cipher.extend_keyword(15) == "TRAINTRAINTRAIN"

def test_extend_keyword_to_length_16(valid_cipher):
    assert valid_cipher.extend_keyword(16) == "TRAINTRAINTRAINT"

def test_separate_character():
    assert separate_character("X", "T") == "E"
    assert separate_character("E", "R") == "N"

def test_decode(valid_cipher):
    assert valid_cipher.decode("XECWQXUIVCRKHWA") == "ENCODEDINPYTHON"
