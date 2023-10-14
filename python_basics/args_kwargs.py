# This is where *args can be really useful,
# because it allows you to pass a varying number of positional arguments.


# Note: that args is just a name.
def add (*integers, **kwargs):
    sum = 0
    for x in integers:
        sum += x

    for arg in kwargs.values():
        print(arg)

    return sum



print(add(1,2,3,4))
print(add(1,2,3,4,5,3,2))
print(add(1,2,name = "myName"))


# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))



