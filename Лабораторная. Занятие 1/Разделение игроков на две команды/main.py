list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

share = len(list_players) // 2    # считаем и делим пополам
one_players = list_players[:share]    # первый список
two_players = list_players[share:]    # второй список

print(one_players)
print(two_players)
