import recursion_challenge

class Test_Factorial:
    def test_001(self):
        assert recursion_challenge.factorial(0) == 1
    def test_002(self):
        assert recursion_challenge.factorial(10) == 3628800
    def test_003(self):
        assert recursion_challenge.factorial(5) == 120