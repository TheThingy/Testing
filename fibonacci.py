#Ask user how many Fibonacci numbers they want to generate
a = int(input("Enter number: "))


def fib(userInput):
    fiblist = []
    for x in range(userInput+1):
        fiblist.append(x)
    return print(fiblist)

fib(a)