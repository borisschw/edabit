


def function1():
    my_variable = [5]
    print("Before function2:", my_variable)
    function2(my_variable)
    print("After function2:", my_variable)

def function2(variable):
    # Modify the variable inside function2
    variable[0] = 10

# Call function1
function1()