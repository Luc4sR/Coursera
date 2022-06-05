def fizzbuzz(x):
    if x % 3 == 0 and x % 5 >= 1:
        return 'Fizz'
    elif x % 5 == 0 and x % 3 >= 1:
        return 'Buzz'
    elif x % 5 == 0 and x % 3 == 0:
        return 'FizzBuzz'
    else:
        return x
