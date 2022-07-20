import unittest
from PALINDROMEPYTHON.src.palindromes import palindrome


class TestPalindrome(unittest.TestCase):
  def test_palindrome_string(self):
    s = "racecar"
    result = palindrome(s)
    self.assertEqual(result,True)


if __name__ == '__main__':
    unittest.main()