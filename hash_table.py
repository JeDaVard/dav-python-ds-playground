class HashTable:
    def __init__(self, size):
        self.data = [[] for i in range(size)]

    def __hash(self, key):
        hashed = 0
        for i in range(len(key)):
            hashed = (hashed + ord(key[i])) % len(self.data)

        return hashed

    def set(self, key, value):
        address = self.__hash(key)
        self.data[address].append([key, value])

    def get(self, key):
        address = self.__hash(key)
        if self.data[address]:
            for item in self.data[address]:
                if item[0] == key:
                    return item[1]

            return None

    def keys(self):
        all_keys = []
        for item in self.data:
            if item:
                all_keys.append(item[0][0])

        return all_keys

    def all(self):
        return self.data


hash_table = HashTable(10)
hash_table.set('grapes', 10000)
hash_table.set('grapes', 10000)
hash_table.set('grapes', 10000)
hash_table.set('grapes', 10000)
hash_table.set('apples', 10000)
hash_table.set('kiwis', 10000)
# print(hash_table.get('grapes'))
# print(hash_table.all())
print(hash_table.keys())
# print(hash_table.get('grapes'))
