# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.
my_list = []
tup1 = ('Shreya','Baidya', 22)
tup2 = ('Shraddha', 'Amatya', 23)
tup3 = ('Alisha', 'Thakuri', 23)
my_list.append(tup1)
my_list.append(tup2)
my_list.append(tup3)
sort = sorted( my_list, key = lambda tup: tup[0])
print(sort)
