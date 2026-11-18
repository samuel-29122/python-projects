class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        total = 0

        for character in key:
            total += ord(character)

        return total

    def add(self, key, value):
        index = self.hash(key)

        if index not in self.collection:
            self.collection[index] = {}

        self.collection[index][key] = value

    def remove(self, key):
        index = self.hash(key)

        if index not in self.collection:
            return

        if key not in self.collection[index]:
            return

        del self.collection[index][key]

        if not self.collection[index]:
            del self.collection[index]

    def lookup(self, key):
        index = self.hash(key)

        if index not in self.collection:
            return None

        return self.collection[index].get(key)
