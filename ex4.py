def calculate_scrabble_score(word):
    score = 0
    for letter in word:
        if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']:
            score += 1
        elif letter in ['D', 'G']:
            score += 2
        elif letter in ['B', 'C', 'M', 'P']:
            score += 3
        elif letter in ['F', 'H', 'V', 'W', 'Y']:
            score += 4
        elif letter == 'K':
            score += 5
        elif letter in ['J', 'X']:
            score += 6
        elif letter in ['Q', 'Z']:
            score += 10
    return score


word = input("Введите слово: ")
score = calculate_scrabble_score(word.upper())
print("Стоймость слова:", score)
