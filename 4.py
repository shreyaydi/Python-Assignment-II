# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?
my_list = ['Ram','Shyam']
print(id(my_list))
my_list.append('Hari')
my_list.append('Krishna')
my_list.append('Laxman')
print(id(my_list))
sort = sorted(my_list)
print(sort[0])
print(sort[1])
