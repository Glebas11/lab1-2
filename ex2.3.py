def create_chessboard(n, m):
    chessboard = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        chessboard.append(row)
    return chessboard


try:
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))

    if n <= 0 or m <= 0:
        raise ValueError("Числа n и m должны быть положительными.")

    board = create_chessboard(n, m)
    for row in board:
        print(" ".join(row))
except ValueError as e:
    print(e)