salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.03  # Ежемесячный рост цен

# Инициализируем переменные
total_needed = 0  # Общая сумма, необходимая для подушки безопасности

# Рассчитываем необходимые средства для каждого месяца
for month in range(months):
    # Если зарплата недостаточна для покрытия расходов
    if spend > salary:
        total_needed += spend - salary  # Вычисляем нехватку и добавляем к общей сумме подушки

    # Увеличиваем расходы на 3% для следующего месяца
    spend *= (1 + increase)

# Округляем до целого числа
total_needed = round(total_needed)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:" ,total_needed )
