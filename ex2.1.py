def is_password_good(password):
    try:
        if len(password) < 8:
            raise ValueError("Пароль слишком короткий. Длина пароля должна быть не менее 8 символов.")

        has_upper = False
        has_digit = False

        for char in password:
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True

        if not has_upper:
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву (верхний регистр).")

        if not has_digit:
            raise ValueError("Пароль должен содержать хотя бы одну цифру.")

        return True

    except ValueError as e:
        print(e)
        return False

    finally:
        print("Проверка пароля завершена.")

password = str(input())
result = is_password_good(password)
print(result)