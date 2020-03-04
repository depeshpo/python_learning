
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value

repeater = Repeater('Hello')

for item in repeater:
    print(item)


# ----------------------------------------------------

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

repeater = Repeater(1)
for item in repeater:
    print(item)


# ------------------------------------------------

class FiniteRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = FiniteRepeater('hello', 5)
for item in repeater:
    print(item)

# next thing -> infinite generators

