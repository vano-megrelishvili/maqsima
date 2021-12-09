class Lists:
    def __init__(self, arr):
        self.arr = arr
        result = self.arr_methods()
        print(f"list - {arr}")
        print(f"sum - {result[0]}")
        print(f"min - {result[1]}")
        print(f"max - {result[2]}")

    def arr_methods(self):
        return sum(self.arr), min(self.arr), max(self.arr)


obj = Lists([1, 2, 3, 4])
