i=0
my_list=[]
for i in range(100):
    my_list.append(i)
    if (len(my_list) == 5):
        print(my_list)
        my_list.clear()

    print(my_list)
