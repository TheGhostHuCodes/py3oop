import py.test

class TestNumbers:
    def test_int_float(self):
        assert 1 == 1.0

    @py.test.mark.xfail()
    def test_int_str(self):
        assert 1 == "1"
