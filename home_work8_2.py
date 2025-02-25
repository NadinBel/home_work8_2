def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return (result, incorrect_data)
def calculate_average(numbers):
    try:
        count_sum = personal_sum(numbers)
        total_result = count_sum[0] / (len(numbers) - count_sum[1])
        return total_result
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
