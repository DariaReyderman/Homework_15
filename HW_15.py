import random

# Exercise 1
print("Exercise 1")
random_list: list[int] = [random.randint(1, 100) for _ in range(50)]
print(random_list)

print('a, numbers above 50', list(filter(lambda x: x > 50, random_list)))
print('b, numbers that are divisible by 7 without remainder', list(filter(lambda x: x % 7 == 0, random_list)))
print('c, 2-digit numbers', list(filter(lambda x: 10 <= x <= 99, random_list)))
print('d, tens equal units', list(filter(lambda x: x // 10 == x % 10, random_list)))
print('e, tens + units = 9', list(filter(lambda x: (x // 10) + (x % 10) == 9, random_list)))
print('f, numbers above the average', list(filter(lambda x: x > (sum(random_list) / len(random_list)), random_list)))
print('g, numbers above the half of the biggest number', list(filter(lambda x: x > max(random_list) / 2, random_list)))

# Exercise 2
print("Exercise 2")
games: list[str] = ["Grand Theft Auto V", "Fortnite", "Overwatch", "Dark Souls", "The Elder Scrolls V: Skyrim"]
print('a', list(filter(lambda game: len(game) > 8, games)))
print('b', list(filter(lambda game: game.upper().startswith('F'), games)))
print('c', list(filter(lambda game: len(game.split()) == 2, games)))
print('d', list(filter(lambda game: 'V' in game.upper(), games)))

# Exercise 3
print("Exercise 3")
rand_list: list[int] = [random.randint(-50, 50) for _ in range(20)]
print(rand_list)
print('a', list(map(lambda x: x ** 3, rand_list)))
print('b, units only', list(map(lambda x: abs(x) % 10, rand_list)))
print('c, Fahrenheit', list(map(lambda x: f"{x * 9 / 5 + 32:.2f}", rand_list)))
print('d Bonus', list(map(lambda x: "positive" if x > 0 else "negative", rand_list)))

# Exercise 4
print("Exercise 4")
fruits: list[str] = ["Mango", "Orange", "Banana", "Apple", "Watermelon", "Grapes", "Pineapple", "Strawberry"]
print('a', list(map(lambda fruit: fruit[::-1], fruits)))
print('b', list(map(lambda fruit: fruit[0], fruits)))
print('c', list(map(lambda fruit: fruit.upper(), fruits)))
print('d', list(map(lambda fruit: fruit[len(fruit) // 2], fruits)))
print('e Bonus', list(map(lambda fruit: fruit + '!' if fruit.endswith('s') else fruit, fruits)))

# Exercise 5
# 1
# The "global" keyword is used within a function to indicate that a variable refers to the global scope
#      (outside the function)
# Using global inside a function can result in loss of control over where and how that variable can be changed,
#      which can lead to bugs and difficulties in debugging. This may further require us to return values from
#      functions instead of modifying global variables.

# 2
# x: int = 1
# def foo():
#     print(x)
#     x = 4
# foo()

# The error occurs because in the foo() function, the variable x is used before it is assigned a value. If you try to
# use a global variable, but within the function, a local variable with the same name assigned, Python treats it as
# local variable, leading to the error, because the local variable is not initialized at the time of the print(x) call.
