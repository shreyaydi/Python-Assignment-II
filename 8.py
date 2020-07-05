# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.


def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True


n = int(input('enter a number'))
print(is_prime(n))
