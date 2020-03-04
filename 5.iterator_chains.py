# generator expressions can be chained together

# -----------------------------------------------------------------

def integers():
    for i in range(1,8):
        yield i

def squared(seq):
    for i in seq:
        yield i*i

def negated(seq):
    for i in seq:
        yield -i


chain1 = integers()
print(list(chain1))

chain2 = squared(integers())
print(list(chain2))

chain3 = negated(squared(integers()))
print(list(chain3))

# ----------------------------------------------------------------------


even_squares = (x*x for x in range(5) if x%2==0)
negated = (-x for x in even_squares)

# see values in even_squares and negative_numbers
print(list(even_squares))
print(list(negated))

