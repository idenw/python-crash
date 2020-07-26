my_dict = {}

for i in (input("please enter a text  :    ")):
    keys = my_dict.keys()
    if i in keys:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
        
my_dict