class BowlingScore:
    def __init__(self):
        self.tuples = []

    def add(self, value1: int, value2: int):
        if len(self.tuples) >= 10:
            raise Exception("List full")
        elif value1 < 0 or value2 < 0:
            raise Exception("Negative values")
        elif value1 + value2 > 10:
            raise Exception("Sum > 10")
        elif not isinstance(value1, int) or not isinstance(value2, int):
            raise Exception("no integer values")
        self.tuples.append((value1, value2))

    def sum(self):
        tuple_sum = 0
        for idx, t in enumerate(self.tuples):
            if idx + 1 < len(self.tuples):
                if t[0] == 10:
                    tuple_sum += sum(self.tuples[idx + 1])
                elif sum(t) == 10:
                    tuple_sum += self.tuples[idx + 1][0]
            tuple_sum += sum(t)
        return tuple_sum

    def pop(self):
        self.tuples.pop()
