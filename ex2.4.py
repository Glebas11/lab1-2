try:
    # Запрос чисел у пользователя
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Попытка выполнить деление
    result = num1 / num2

except ZeroDivisionError:
    print("Ошибка: Деление на ноль.")
except ValueError:
    print("Ошибка: Введены некорректные данные.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Завершение программы.")

# Если исключения не возникло, выведем результат
if 'result' in locals():
    print(f"Результат: {result}")