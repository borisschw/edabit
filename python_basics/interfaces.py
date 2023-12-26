# Define a common interface
class CommonInterface:
    def function1(self):
        print("CommonInterface - Function 1")

    def function2(self):
        print("CommonInterface - Function 2")


# Implement the interface in ClassA
class ClassA(CommonInterface):
    def function1(self):
        print("ClassA - Function 1")

    def function2(self):
        print("ClassA - Function 2")

# Implement the interface in ClassB
class ClassB(CommonInterface):
    def function1(self):
        print("ClassB - Function 1")

    # def function2(self):
    #     print("ClassB - Function 2")

# Example usage
if __name__ == "__main__":
    # Create instances of ClassA and ClassB
    object_a = ClassA()
    object_b = ClassB()

    # Call functions using the common interface
    object_a.function1()
    object_a.function2()

    object_b.function1()
    object_b.function2()
