import random

numbers = ()
for _ in range(10):
    numbers += (random.randint(1, 10),)
print(numbers)
max_number = max(numbers)
min_number = min(numbers)

print("Максимальный элемент:", max_number)
print("Минимальный элемент:", min_number)