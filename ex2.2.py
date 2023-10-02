def process_input():
    try:
        user_input = input("Введите данные: ")

        if user_input.isdigit():
            data = int(user_input)
            if data <= 1:
                raise ValueError("Число не является простым.")
            is_prime = True
            for i in range(2, int(data ** 0.5) + 1):
                if data % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("Число является простым.")
            else:
                print("Число не является простым.")

        elif all(char.isdigit() or char.isspace() or char == '-' for char in user_input):
            data = [int(item) for item in user_input.split()]
            count = 0
            for item in data:
                if item < 0:
                    break
                count += 1
            print(f"Количество элементов до первого отрицательного: {count}")

        elif all(char.isalpha() or char.isspace() or char.isdigit() for char in user_input):
            reversed_str = user_input[::-1]
            print(f"Строка в обратном порядке: {reversed_str}")

            digit_sum = sum(int(char) for char in user_input if char.isdigit())
            print(f"Сумма цифр в строке: {digit_sum}")

        else:
            raise ValueError("Неизвестный тип данных.")

    except ValueError as e:
        print(e)

    finally:
        print("Обработка данных завершена.")

process_input()