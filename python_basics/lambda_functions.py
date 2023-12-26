

class test():

    def __init__(self, x):
        self.x = x
        self.remove_characters = lambda s: float(''.join(filter(lambda c: c.isdigit() or c == "-" or c == ".", s)))


    def __call__(self, y):
        return self.x + y






if __name__ == "__main__":
    t = test(1)
    mystr = "-20mah"
    mystr = ""
    # print(t(2))
    # t.remove_characters("-20C")
    if (mystr):
        print(t.remove_characters(mystr))
    else:
        print("Empty string")