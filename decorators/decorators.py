class TestClass:
    def __init__(self):
        self.attr1 = 1
        self.attr2 = 2
        # self.attr3 = 3


# PLC connection decoration:
def requires_connection(func):
    # print function name:
    print(func.__name__)
    # Wrapper function:
    def connectDo(*args, **kw):

        try:
            # Verify connection:
            print("connect")

            # Call function:

            result = func(*args, **kw)
            print("result: ", result)
            # Return result:
            return result

        finally:
            print("Lock released")


    # Return wrapper function:
    return connectDo



@requires_connection
def func(obj):

    if hasattr(obj, "attr1") is False:
        return "attr3 not found"

    return None




#main function
def main():
    # obj = TestClass()
    obj = None
    print(func(obj))




if __name__ == "__main__":
    main()