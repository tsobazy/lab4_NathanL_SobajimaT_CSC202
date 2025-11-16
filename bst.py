import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

# 2.1
BinTree : TypeAlias = Union['BTNode', None]

@dataclass(frozen=True)
class BTNode:
    value : Any
    left : BinTree
    right : BinTree

@dataclass(frozen=True)
class BST:
    comes_before : Callable[[Any, Any], bool]
    BT : BinTree 


# finds whether a binary search tree is empty (True means empty)
def is_empty(t : BST) -> bool:
    if t.BT is None:
        return True
    return False

# adds a given value to a binary search tree
def insert(t : BST, val : Any) -> BST:
    decide = t.comes_before
                 
    def insert_helper(t : BinTree, val : Any, decide : Callable[[Any, Any], bool]) ->  BinTree:
        if t is None:
            return BTNode(val, None, None)
        if decide(val, t.value):
            return BTNode(t.value, insert_helper(t.left, val, decide), t.right)
        if decide(t.value, val):
            return BTNode(t.value, t.left, insert_helper(t.right, val, decide))
        return t
    
    return BST(decide, insert_helper(t.BT, val, decide))

# finds whether a value is in a binary search tree (True means value found in tree)
def lookup(t : BST, val : Any) -> bool:
    decide = t.comes_before

    def lookup_helper(t : BinTree, val : Any, decide : Callable[[Any, Any], bool]) -> bool:
        if t is None:
            return False
        
        if not decide(val, t.value) and not decide(t.value, val):
            return True
        if decide(val, t.value):
            return lookup_helper(t.left, val, decide)
        if decide(t.value, val):
            return lookup_helper(t.right, val, decide)
        return False
    
    return lookup_helper(t.BT, val, decide)

# deletes, if possible, a value from a binary search tree and generates new tree
def delete(t : BST, val : Any) -> BST:
    decide = t.comes_before

    def delete_helper(t : BinTree, val : Any) -> BinTree:
        if t is None:
            return None
        
        if not decide(val, t.value) and not decide(t.value, val):
            if t.left is None:
                return t.right
            if t.right is None:
                return t.left
        
            success = t.right
            while success.left is not None:
                success = success.left
            new_right = delete_helper(t.right, success.value)
            return BTNode(success.value, t.left, new_right)

        if decide(val, t.value):
            return BTNode(t.value, delete_helper(t.left, val), t.right)
        else:
            return BTNode(t.value, t.left, delete_helper(t.right, val))
        
    return BST(decide, delete_helper(t.BT, val))
