# Исходные данные
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_needed = 0
current_spend = spend


for month in range(months):

    deficit = max(0, current_spend - salary)
    total_needed += deficit
    current_spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total_needed))
