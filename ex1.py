# сколько четны и нечетных
a = int(input())

even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print(f'Even: {even}, odd: {odd}')
