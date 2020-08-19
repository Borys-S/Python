# Task 1
# Write a Python program to detect the number of local variables declared in a function.


# def inside_func():
#   a = [54, 65, 'jhgk']
#   b = 656462
#   c = 'string'
#
#
# print(f'Function "{inside_func.__name__}" has {inside_func.__code__.co_nlocals} variables inside.')


# Task 2
# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)


def tax(x):
    def percent(y):
        return (y / 100 * x)

    return percent


duty = tax(18.5)
print(duty(int(input('Enter your salary: '))))
