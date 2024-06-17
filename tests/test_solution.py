import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solution import minEatingSpeed


def test_minEatingSpeed():
    # Test case 1
    piles = [3, 6, 7, 11]
    h = 8
    assert minEatingSpeed(piles, h) == 4

    # Test case 2
    piles = [30, 11, 23, 4, 20]
    h = 5
    assert minEatingSpeed(piles, h) == 30

    # Test case 3
    piles = [30, 11, 23, 4, 20]
    h = 6
    assert minEatingSpeed(piles, h) == 23

    # Additional test cases
    piles = [1, 1, 1, 1]
    h = 4
    assert minEatingSpeed(piles, h) == 1

    piles = [1000000000]
    h = 2
    assert minEatingSpeed(piles, h) == 500000000

    piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    h = 15
    assert minEatingSpeed(piles, h) == 5
