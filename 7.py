# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.
tup_list = [('Shreya','Baidya',22),('Shraddha', 'Amatya', 23),('Alisha', 'Thakuri', 23),('Ram','Sharma',None)]
age = []
for i in range(len(tup_list)):
    if tup_list[i][2] is not None:
        age.append(tup_list[i][2])
avg = sum(age)/len(age)
for i in range(len(tup_list)):
    name = tup_list[i][0] + ' ' + tup_list[i][1]
    print(name)
    if tup_list[i][2] is not None:
        if tup_list[i][2] < avg:
            print('Young')
        else:
            print('Old')
