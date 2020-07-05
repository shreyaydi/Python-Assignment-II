# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def conv(my_string, seperator):
    var = [my_string[0].lower()]
    for x in my_string[1:]:
        if x in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            var.append(seperator)
            var.append(x.lower())
        else:
            var.append(x)
    return ''.join(var)


my_string = 'ThisIsCamelCased'
print(conv(my_string, '_'))
print(conv(my_string, '-'))
