from format_string import format_string

def test_format_string_returns_default_title_formatting():
    hello_string = "hello world, how are you today?"
    assert format_string(hello_string) == hello_string.title()
