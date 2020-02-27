from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderedDict = OrderedDict()
        # ordered dict needs to evict from the first position

    def get(self, key: int) -> int:
        if key not in self.orderedDict.keys():
            return -1

        # reinsert items into the front
        self.orderedDict.move_to_end(key)
        return self.orderedDict[key]

    def put(self, key: int, value: int) -> None:
        self.orderedDict[key] = value
        self.orderedDict.move_to_end(key)

        if len(self.orderedDict) > self.capacity:
            self.orderedDict.popitem(0)



if __name__ == "__main__":

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    output = cache.get(1)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(10)
    commands = ["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
                "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put",
                "get",
                "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put",
                "put",
                "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get",
                "put",
                "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put",
                "put",
                "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put",
                "put",
                "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    data = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
            [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3],
            [10, 11], [8],
            [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
            [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26],
            [8, 17],
            [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
            [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
            [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1],
            [2, 2],
            [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    output = []
    for command_i in range(len(commands)):
        if commands[command_i] == "put":
            key, value = data[command_i]
            cache.put(key, value)
            output.append(None)
        else:
            key = data[command_i][0]
            value = cache.get(key)
            output.append(value)

    assert output == [None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1,
                      12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1,
                      24, None, None, 18, None, None, None, None, -1, None, None, 18, None, None, -1, None, None, None,
                      None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, -1, None, None, None, None, 29, None,
                      None, None, None, 17, 22, 18, None, None, None, -1, None, None, None, 20, None, None, None, -1,
                      18, 18, None, None, None, None, 20, None, None, None, None, None, None, None]
