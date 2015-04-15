from secret_string import SecretString

def pytest_funcarg__secret_string(request):
    return SecretString("ACME: Top Secret", "antwerp")

def test_secret_string_with_correct_decrypt_returns_secret(secret_string):
    assert secret_string.decrypt(secret_string._SecretString__pass_phrase) == \
        secret_string._SecretString__plain_string

def test_secret_string_with_incorrect_decrypt_returns_blank(secret_string):
    assert secret_string.decrypt("not_the_password") == ""

def test_secret_string_is_not_very_secret(secret_string):
    assert secret_string._SecretString__plain_string == \
    secret_string.decrypt(secret_string._SecretString__pass_phrase)
