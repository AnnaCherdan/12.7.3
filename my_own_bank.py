# Выполнила Черданцева Анна, QAP - 73.
deposit = input('Введите сумму вклада в рублях: ') # пользователь вводит сумму вклада на клавиатуре.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

banks = list(per_cent.keys()) # Формирование списка банков по ключам из словаря per_cent.
earnings = list(per_cent.values()) # Формирование списка ставок по значениям объектов из словаря per_cent.

tkb = round(int(deposit) / 100 * (earnings[0])) # Вычисление дохода банка с индексом 0 с округлением до целого.
scb = round(int(deposit) / 100 * (earnings[1])) # Вычисление дохода банка с индексом 1 с округлением до целого.
vtb = round(int(deposit) / 100 * (earnings[2])) # Вычисление дохода банка с индексом 2 с округлением до целого.
sber = round(int(deposit) / 100 * (earnings[3])) # Вычисление дохода банка с индексом 3 с округлением до целого.

print((f'\nЗа год накопления составят:\nБанк {banks[0]} - {tkb} рублей\nБанк {banks[1]} - {scb} '
      f'рублей\nБанк {banks[2]} - {vtb} рублей\n{banks[3]} банк - {sber} рублей\n'))
all_banks = [tkb, scb, vtb, sber] # создание списка дохода в банках для вычисления max(доход)
max_earnings = max(all_banks)
print(f'Максимальная сумма, которую Вы можете заработать: {max_earnings} рублей.')