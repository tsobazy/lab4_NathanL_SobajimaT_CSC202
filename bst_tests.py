import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

num_bst = BST(comes_before_function, BTNode(5, BTNode(3, 
                                                      BTNode(2, None, None), 
                                                      BTNode(4, None, None)),
                                                BTNode(11, None, BTNode(15, None, None))))

alph_bst = BST(comes_before_function, BTNode('h', BTNode('b', 
                                                      BTNode('a', None, None), 
                                                      BTNode('f', None, None)),
                                                BTNode('x', 
                                                       BTNode('n', None, None), 
                                                       BTNode('z', None, None))))

class BSTTests(unittest.TestCase):
   def test_is_empty(self):
     self.assertEqual(False, is_empty(num_bst))
     self.assertEqual(True, is_empty(BST(comes_before_function, None)))
   
if (__name__ == '__main__'):
 unittest.main() 