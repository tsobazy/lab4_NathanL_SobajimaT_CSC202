import sys
import unittest
from typing import *
from dataclasses import dataclass
import math 
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)

from bst import *

TREES_PER_RUN : int = 10000

def example_graph_creation() -> None:
    # Return log-base-2 of 'x' + 5.
    def f_to_graph( x : float ) -> float:
        return math.log2( x ) + 5.0
        
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
        
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
        
    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

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

# generates binary search tree with n random values from 0 to 1
def random_tree(n : int) -> BST:
    count = 0
    nums : list[float] = []
    while count != n:
       rand = random.random()
       nums.append(rand)
       count += 1

    t = BST(comes_before_function, None)
    for num in nums:
       t = insert(t, num)
    return t

# finds longest height
def height(tree : BinTree) -> int:
    if tree is None:
        return 0
    else:
        return 1 + max(height(tree.left), height(tree.right))

# generate graph of average tree height as a function of N where n_max is 49
def random_tree_graph() -> None:
    y_vals : list[float] = []
    for i in range(1, 50):
        tot_h = 0
        for _ in range(TREES_PER_RUN):
            tree = random_tree(i - 1)
            tot_h += height(tree.BT)
        h = tot_h / TREES_PER_RUN
        y_vals.append(round(h, 2))
    
    x_coords : list[int] = [int(i - 1) for i in range(1, 50)]
    y_coords : list[float] = y_vals

    x_numpy : np.ndarray = np.array(x_coords)
    y_numpy : np.ndarray = np.array(y_coords)
        
    plt.plot( x_numpy, y_numpy, label = 'n_max = 49')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Average Tree Height as a Function of N')
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

class BSTTests(unittest.TestCase):
    def test_n_max(self):
        for _ in range(TREES_PER_RUN):
            tree = random_tree(49)
            h = height(tree.BT)

if (__name__ == '__main__'):
    random_tree_graph()