# generator expressions ( stay away from
# any generator expression that includes more than two levels of nest-
# ing.)
# list comprehension vs generator expressions
# we use small bracket instead of square bracket

list_comprehension = [i*i for i in range(4)]
generator_expression = (i*i for i in range(4))

print(next(generator_expression)) # calling next item
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression)) # StopIteration


print([*generator_expression]) # gives result in list
print(*generator_expression) # result without list (if items are consumed it will result empty)

even_squares = (x*x for x in range(5) if x%2==0)
# print([*even_squares])
for item in even_squares:
    print(item)

## (expression
#   for item in collection
#   if condition)

# # SIMILAR TO
# def generator():
#     for item in collection:
#         if condition:
#             yield expression

## NEXT iterator chain
