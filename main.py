from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 128) -> None:
        self.od: OrderedDict[str, int] = OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> int:
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key: str, value: int) -> None:
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)  # last=False FIFO


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.put('a', 1)
    lru.put('b', 2)
    lru.put('c', 3)
    lru.put('d', 4)
    assert list(lru.od.keys()) == ['b', 'c', 'd']
