import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

#2.1
BinTree: TypeAlias = Optional["BTNode"]

@dataclass(frozen=True)
class BTNode:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BST:
    comes_before: Callable[[Any, Any], bool]
    BT: BinTree 


# returns True if the BST is empty, False otherwise.
def is_empty(t: BST) -> bool:
    if t.BT is None:
        return True
    return False

# adds a given value to the binary search tree
def insert(t: BST, val: Any) -> BST:
    decide = t.comes_before  # user-supplied comparator stored on the tree
                 
    def insert_helper(t: BinTree, val: Any, decide: Callable[[Any, Any], bool] ) ->  BinTree:
        if t is None:
            return BTNode(val, None, None)
        if decide(val, t.value):
            return BTNode(t.value, insert_helper(t.left, val, decide), t.right)
        if decide(t.value, val):
            return BTNode(t.value, t.left, insert_helper(t.right, val, decide))
        return t
    return BST(decide, insert_helper(t.BT, val, decide))

# returns True if it is stored in the tree and False otherwise
def lookup
    

