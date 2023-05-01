# Selection sort in Python
# Time complexity O(n*n)
# sorting by finding max_index
def selection_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        max_index = 0
        for j in range(1, i+1):
            if numbers[j] > numbers[max_index]:
                max_index = j
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    return numbers


numbers = [3, 7, 5, 4, 2, 1, 6]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)


def binary_search(text: list, target: str) -> str:
    # Initialize start and end indices
    start = 0
    end = len(text) - 1

    # Binary search loop
    while start <= end:
        mid = (start + end) // 2  # Find the middle index
        if target == text[mid]:
            return text[mid]  # Target found, return the word
        elif target < text[mid]:
            end = mid - 1  # Target is in the left half
        else:
            start = mid + 1  # Target is in the right half

    return None  # Target not found, return None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return len(key) % self.size
        else:
            raise TypeError("Key must be either an integer or a string.")

    def put(self, key, data):
        h = self.__my_hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][i] = (key, data)
                return
        self.table[h].append((key, data))

    def get(self, key):
        h = self.__my_hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return None
