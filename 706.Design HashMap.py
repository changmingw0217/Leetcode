class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 2048
        self.buckets = [[] for i in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.buckets[key % self.capacity]

        if self.get(key) == -1:
            bucket.append([key, value])
        else:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i][1] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self.buckets[key % self.capacity]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.buckets[key % self.capacity]
        pair = [key, self.get(key)]
        if pair[1] != -1:
            bucket.remove(pair)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)