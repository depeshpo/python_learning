# class based
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

repeater = Repeater('hello')
for item in repeater:
    print(item)


# function based
def repeater(value):
    while True:
        yield value

# for item in repeater('Hello'):
    # print(item)

result = repeater("hello0")
print(next(result)) # we can do next operation on this.
print(next(result)) # we can do next operation on this.
print(type(result))


# ----------------------------------------------

def finite_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
repeater = finite_repeater('Hello', 12)
for item in repeater:
    print(item)



# generator expression next
