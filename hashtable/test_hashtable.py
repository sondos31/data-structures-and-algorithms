import pytest
from hash_table import Node, LinkedList,HashTable

# Setting a key/value to your hashtable results in the value being in the data structure
def test_set_to_Hashtable():
    Hash = HashTable(10)
    Hash.set('one', 1)
    actual = Hash.contains('one')
    expected = True
    assert actual == expected

# Retrieving based on a key returns the value stored
def test_get():
    Hash = HashTable(10)
    Hash.set('one',1)
    Hash.set('two',2)
    actual = Hash.get('one')
    expected = 1
    assert actual == expected

# Successfully returns null for a key that does not exist in the hashtable
def test_get():
    Hash = HashTable(10)
    Hash.set('one',1)
    Hash.set('two',2)

    assert Hash.get('three') == None

#Successfully returns a list of all unique keys that exist in the hashtable

def test_Key():
    Hash = HashTable(10)
    Hash.set('one',1)
    Hash.set('two',2)
    actual=Hash.key()
    expected=['one','two']
    assert actual == expected


#Successfully handle a collision within the hashtable

def test_collision():
    Hash = HashTable(10)
    Hash.set('one',1)
    Hash.set('two',2)

    assert Hash.buckets[Hash.hash('one')].head.data == ('one',1)
    assert Hash.buckets[Hash.hash('two')].head.data == ('two',2)


#Successfully retrieve a value from a bucket within the hashtable that has a collision

def test_get_with_collision():
    Hash = HashTable(10)
    Hash.set('one',1)
    Hash.set('two',2)
    assert Hash.get('two') == 2

#Successfully hash a key to an in-range value
def test_hash_key():
    Hash = HashTable(10)

    assert  Hash.hash('one')<= 1014