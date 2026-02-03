#LIST
my_list = ["Apple", "Banana", "Cherry", "Orange"]
print(my_list)
print(my_list[0:2])
if "Cherry" in my_list:
    print("Cherry in the list")
my_list.insert(2, "Watermelon")
my_list.pop(2)
del my_list
my_list.clear()

for x in my_list:
    print(x)


new_list = [x for x in my_list if "A" in x]

newlist = [x if x != "Banana" else "Orange" for x in my_list]
