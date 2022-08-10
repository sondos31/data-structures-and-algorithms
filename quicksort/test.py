from main import QuickSort
import pytest

def test_revers_sort():
    assert QuickSort([20,18,12,8,5,-2],0,5)== [-2,5,8,12,18,20]


def test_few_uniques():
    assert QuickSort([5,12,7,5,5,7],0,5)== [5,5,5,7,7,12]

def test_nearly_sorted():
    assert QuickSort([2,3,5,7,13,11],0,5)== [2,3,5,7,11,13]