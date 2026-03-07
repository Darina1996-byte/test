def month_to_season(month_number):
    if not (1 <= month_number <= 12):
        return "Неверный номер месяца"
    if month_number in [12, 1, 2]:
        return "Зима"
    elif month_number in [3, 4, 5]:
        return "Весна"
    elif month_number in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"

print(month_to_season(2)) 
print(month_to_season(13))