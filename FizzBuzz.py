def FizzBuzz():
    for i in range(1, 100):
        print(i)
        if i % 3 == 0:
            print (i, "Fizz")
        if i % 5 == 0:
            print (i, "Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print (i, "FizzBuzz")
FizzBuzz()