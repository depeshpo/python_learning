languages = ["Python", "Java", "Swift", "C"]

iterator_obj = iter(languages) # languages is an iterable, need to pass iter() to make it iterator

print(next(iterator_obj)) # passing next() method to the iterator object to get next item in the iterator
print(next(iterator_obj)) # and next
print(next(iterator_obj)) # and next
print(next(iterator_obj)) # and next
print(next(iterator_obj)) # see the StopIteration exception, which tells the iterator object can not find next item in the iterator object

# ---------------------------------------------------------------------
### Check object is iterable or not

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(1, is_iterable(1))
print('1', is_iterable('1'))

# ------------------------------------------------------------------
## code how for loop works
# create an iterator object from that iterable
iterable = [1,2,3,4]

iter_obj = iter(iterable)

# # infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

# ----------------------------------------------------------------
