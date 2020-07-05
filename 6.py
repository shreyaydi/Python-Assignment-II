# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
my_list = ['Ram','Shyam','Hari','Krishna','Laxman']


def find_john(x):
    for i in x:
        if i == 'John':
            return 'Found'
        else:
            return 'Not found'


print(find_john(my_list))
