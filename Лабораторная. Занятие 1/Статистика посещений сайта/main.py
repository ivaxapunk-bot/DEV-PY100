users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

unique_users = set(users)

new_users = {"Общее количество": 0, "Уникальные посещения": 0}
new_users["Общее количество"] = len(users)
new_users["Уникальные посещения"] = len(unique_users)
print(new_users)
