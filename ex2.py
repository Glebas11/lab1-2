a = str(input())
pair_lower = 0
pair_upper = 0
for i in range(1, len(a)):
    print(a[i-1], a[i])
    if a[i-1].islower() and a[i].islower():
        pair_lower += 1
    if a[i - 1].isupper() and a[i].isupper():
        pair_upper += 1
print('верхний регистр:', pair_upper)
print('нижний регистр', pair_lower)