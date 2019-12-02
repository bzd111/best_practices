import unittest

# from best_practices.main import LRUCache
from main import LRUCache


class TestLRU(unittest.TestCase):
    def test_lru(self) -> None:
        lru = LRUCache(3)
        lru.put('a', 1)
        lru.put('b', 2)
        lru.put('c', 3)
        lru.put('d', 4)
        assert list(lru.od.keys()) == ['b', 'c', 'd']
