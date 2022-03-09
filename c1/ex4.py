def get_nth_fibonacci(n):
    for i in range(n):
        no1 = 0
        no2 = 1
        if n < 0:
            return("Incorrect n")
        elif n ==0:
            return 0
        else:
            for _ in range(1, n):
                sum = no1 + no2
                no1 = no2
                no2 = sum
            return sum

print(get_nth_fibonacci(12))

def get_nthFibonacci_cycle(n):
        if n < 0:
            return("Incorrect n")
        elif n ==0:
            return 0
        else:
            no1 = 0
            no2 = 1
            sum = no1 + no2
            return 0 + 1 get_nthFibonacci_cycle(n +)

print(get_nthFibonacci_cycle(12))