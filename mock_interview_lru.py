from collections import deque 

class LRUCache:

    def __init__(self, capacity: int):
        self._len = capacity
        self._que = deque()
        self._table = dict()

    def put(self, key: int, value: int) -> None:
        if key in self._table:
            self._table[key]=value
            self._que.remove(key)
            self._que.append(key)
        elif self._len == len(self._que):
            old_key = self._que.popleft()
            del self._table[old_key]
        self._table[key] = value
        self._que.append(key)

    def get(self, key: int) -> int:
        value = self._table.get(key, -1)
        if value != -1:
            self._que.remove(key)
            self._que.append(key)
        return value