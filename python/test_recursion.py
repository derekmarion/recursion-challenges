import recursion_challenge

class Test_Factorial:
    def test_001(self):
        assert recursion_challenge.factorial(0) == 1
    def test_002(self):
        assert recursion_challenge.factorial(10) == 3628800
    def test_003(self):
        assert recursion_challenge.factorial(5) == 120

class Test_Palindrome:
    def test_001(self):
        assert recursion_challenge.palindrome('racecar') == True
    def test_002(self):
        assert recursion_challenge.palindrome('noon') == True
    # def test_003(self):
    #     assert palindrome('ciVic') == True
    def test_004(self):
        assert recursion_challenge.palindrome('nice') == False
    # def test_005(self):
    #     assert palindrome(434) == True
    # def test_006(self):
    #     assert palindrome(123) == False
    def test_007(self):
        assert recursion_challenge.palindrome('bomb') == False

    # def test_008(self):
    #     assert palindrome('Sore was I ere I saw Eros.') == True
    # def test_009(self):
    #     assert palindrome('A man, a plan, a canal -- Panama') == True