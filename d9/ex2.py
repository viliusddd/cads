# Sukurti programą, kuri:
# • Sukurtų sąrašą iš skaičių nuo 0 iki 50
# • Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# • Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# • Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
# • Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą,
# mažiausią ir didžiausią skaičių, vidurkį, medianą
# • Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
# Patarimai:
# • Naudoti map, filter arba comprehension, sum, min, max, mean,
# median, %
# • from statistics import mean, median

# • Sukurtų sąrašą iš skaičių nuo 0 iki 50
# nums = [i for i in range(0, 51)]
nums = list(range(0, 50 + 1))

# • Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# print([num * 10 for num in nums])
print(list(map(lambda x: x * 10, nums)))

# • Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# print([num for num in nums if not(num % 7)])
print(list(filter(lambda x: not(x  % 7), nums)))

# • Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
# squared = [num ** 2 for num in nums]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# • Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą,
# mažiausią ir didžiausią skaičių, vidurkį, medianą

from statistics import mean, median

print(sum(nums), min(nums), max(nums), mean(nums), median(nums))

# • Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
# print([sorted(squared)[::-1]])
print(sorted(squared, reverse=True))
