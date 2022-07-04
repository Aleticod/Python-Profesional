# Test de methods

import unittest
from unittest import TestCase
from palindrome import is_palindrome
from prime import is_prime


class TestingFuntions (TestCase):
    # Thes to know if the methods work well

    def test_is_palindrome(self):
        # Testing is_palindrome() method

        self.assertEqual(is_palindrome('Ligar es ser agil '), True)
        self.assertEqual(is_palindrome('Arepera'), True)
        self.assertEqual(is_palindrome('No es palindrome'), False)
    
    
    def test_is_prime(self):
        # Testing is_prime()  method
        self.assertEqual(is_prime(100), False)
        self.assertEqual(is_prime(13), True)


if __name__ == '__main__':
    unittest.main()
