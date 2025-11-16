import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
sys.setrecursionlimit(10**6)

from bst import *

# data defintion for Point2
@dataclass(frozen = True)
class Point2:
     x : float
     y : float

# comes before functions
def comes_before_function(a : Any, b : Any) -> bool:
    return a < b

def dist_comes_before_function(a : Point2, b : Point2) -> bool:
      return math.hypot(a.x, a.y) < math.hypot(b.x, b.y)

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

dist_bst = BST(dist_comes_before_function, BTNode(Point2(3, 4), BTNode(Point2(1, 1), None,
                                                                       BTNode(Point2(2, 2), None, None)),
                                                  BTNode(Point2(0, 6), None, None)))

class BSTTests(unittest.TestCase):
      def test_is_empty(self):
            self.assertEqual(False, is_empty(num_bst))
            self.assertEqual(True, is_empty(BST(comes_before_function, None)))

      def test_num(self):
            # testing insert function
            new_num = BST(comes_before_function, None)
            for n in [5, 3, 11, 2, 4, 15]:
                 new_num = insert(new_num, n)
            self.assertEqual(num_bst, new_num)

            # testing lookup function
            self.assertEqual(True, lookup(num_bst, 11))
            self.assertEqual(False, lookup(num_bst, 67))

            # testing delete function
            del_num = BST(comes_before_function, None)
            for n in [5, 3, 6, 11, 2, 4, 15]:
                 del_num = insert(del_num, n)
            self.assertEqual(num_bst, delete(del_num, 6))

      def test_alph(self):
            # testing insert function
            new_alph = BST(comes_before_function, None)
            for n in ['h', 'b', 'x', 'a', 'f', 'n', 'z']:
                 new_alph = insert(new_alph, n)
            self.assertEqual(alph_bst, new_alph)

            # testing lookup function
            self.assertEqual(True, lookup(alph_bst, 'x'))
            self.assertEqual(False, lookup(alph_bst, 'e'))

            # testing delete function
            del_alph = BST(comes_before_function, None)
            for n in ['h', 'b', 'p', 'x', 'a', 'f', 'n', 'z']:
                 del_alph = insert(del_alph, n)
            self.assertEqual(alph_bst, delete(del_alph, 'p'))

      def test_dist(self):
            # testing insert function
            new_dist = BST(dist_comes_before_function, None)
            for n in [Point2(3, 4), Point2(1, 1), Point2(0, 6), Point2(2, 2)]:
                new_dist = insert(new_dist, n)
            self.assertEqual(dist_bst, new_dist)

            # testing lookup function
            self.assertEqual(True, lookup(dist_bst, Point2(0, 6)))
            self.assertEqual(False, lookup(dist_bst, Point2(1, 2)))

            # testing delete function
            del_dist = BST(dist_comes_before_function, None)
            for n in [Point2(3, 4), Point2(3, 2), Point2(1, 1), Point2(0, 6), Point2(2, 2)]:
                del_dist = insert(del_dist, n)
            self.assertEqual(dist_bst, delete(del_dist, Point2(3, 2)))

if (__name__ == '__main__'):
      unittest.main() 