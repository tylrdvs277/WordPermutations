# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Assignment 1
# Term:        Fall 2017

import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_1(self):
        self.assertEqual(perm_lex.perm_gen_lex("ab"),["ab","ba"])

    def test_perm_gen_lex_2(self):
    	self.assertEqual(perm_lex.perm_gen_lex("a"),["a"])

    def test_perm_gen_lex_3(self):
    	self.assertEqual(perm_lex.perm_gen_lex(""),[])

    def test_perm_gen_lex_4(self):
    	result = ["abc", "acb", "bac", "bca", "cab", "cba"]
    	self.assertEqual(perm_lex.perm_gen_lex("abc"),result)

if __name__ == "__main__":
        unittest.main()