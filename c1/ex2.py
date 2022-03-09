# Parasyti funkcija, kuri atspausdintu n skaiciu, kurie dalinasi is 7 is pirmu r skaiciu saraso

def get_first_numbers(num, nums):
    correct = []
    for i in range(1, nums + 1):
        if i % num == 0:
            print(i)
            correct.append(i)
            if len(correct) == 7:
                break
    return correct

print(get_first_numbers(7, 200))
