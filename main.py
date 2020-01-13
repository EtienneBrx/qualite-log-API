class CoupleOperator:
    def __init__(self):
        self.tuples = []

    def add(self, value1: int, value2: int):
        self.tuples.append((value1, value2))

    def sum(self):
        tuple_sum = 0
        for t in self.tuples:
            for value in t:
                tuple_sum += value
        return tuple_sum

    def pop(self):
        self.tuples.pop()
