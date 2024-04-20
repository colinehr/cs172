"""Unit tests for the ArrayList class."""

__author__ = 'Peter Drake, Alain Kägi, and Colin Ehr'

import pytest
from abstract_list import AbstractList
from array_list import ArrayList

def test_is_initially_empty():
    test_list = ArrayList()
    assert str(test_list) == '[]'

def test_append():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert str(test_list) == '[5, 2, 8]'

def test_clear():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list.clear()
    assert str(test_list) == '[]'

def test_contains_finds_first_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert 5 in test_list

def test_contains_finds_last_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert 8 in test_list

def test_contains_finds_intermediate_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert 2 in test_list

def test_contains_does_not_find_absent_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert 4 not in test_list

def test_extend():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list2 = ArrayList()
    test_list2.append(3)
    test_list2.append(7)
    test_list.extend(test_list2)
    assert str(test_list) == '[5, 2, 8, 3, 7]'

def test_extend_is_generic():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list2 = [3, 7]
    test_list.extend(test_list2)
    assert str(test_list) == '[5, 2, 8, 3, 7]'

def test_getitem():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert test_list[2] == 8

def test_getitem_indexerror_too_big():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    with pytest.raises(IndexError) as _:
        test_list[3]

def test_getitem_indexerror_too_small():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    with pytest.raises(IndexError) as _:
        test_list[-1]

def test_find_index_of_first_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert test_list.index_of(5) == 0

def test_find_index_of_last_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert test_list.index_of(8) == 2

def test_find_index_of_intermediate_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert test_list.index_of(2) == 1

def test_do_not_find_index_of_absent_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    with pytest.raises(ValueError) as _:
        test_list.index_of(4)

def test_find_first_index_of_repeated_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(7)
    test_list.append(2)
    test_list.append(8)
    assert test_list.index_of(2) == 1

def test_insert():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(7)
    test_list.insert(2, 9)
    assert str(test_list) == '[5, 2, 9, 7]'

def test_insert_after_end():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(7)
    test_list.insert(len(test_list), 9)
    assert str(test_list) == '[5, 2, 7, 9]'

def test_insert_on_empty_list():
    test_list = ArrayList()
    test_list.insert(0, 9)
    assert str(test_list) == '[9]'

def test_pop_last_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list.pop()
    assert str(test_list) == '[5, 2]'

def test_pop_first_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert test_list.pop(0) == 5
    assert str(test_list) == '[2, 8]'

def test_pop_intermediate_item():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list.pop(1)
    assert str(test_list) == '[5, 8]'

def test_setitem():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list[2] = 7
    assert str(test_list) == '[5, 2, 7]'

def test_setitem_index_too_big():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    with pytest.raises(IndexError) as _:
        test_list[3] = 7

def test_setitem_index_too_small():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    with pytest.raises(IndexError) as _:
        test_list[-1] = 7

def test_len():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    assert len(test_list) == 3

def test_equals():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list2 = ArrayList()
    test_list2.append(5)
    test_list2.append(2)
    assert test_list != test_list2
    test_list2.append(8)
    assert test_list == test_list2

def test_equals_after_deletion():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    test_list2 = ArrayList()
    test_list2.append(5)
    test_list2.append(2)
    test_list2.append(8)
    test_list2.append(9)
    test_list2.pop()
    assert test_list == test_list2

def test_is_iterable():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    sum = 0
    for n in test_list:
        sum += n
    assert sum == 15

def test_iterate_twice():
    test_list = ArrayList()
    test_list.append(5)
    test_list.append(2)
    test_list.append(8)
    sum = 0
    for n in test_list:
        for m in test_list:
            sum += n
            sum += m
    assert sum == 90

def test_is_generic():
    test_list = ArrayList()
    test_list.append('eggs')
    test_list.append('bread')
    test_list.append('tea')
    assert str(test_list) == '[eggs, bread, tea]'

def test_implements_abstractlist():
    assert isinstance(ArrayList(), AbstractList)