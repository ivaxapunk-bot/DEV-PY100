
def find_common_participants(first_group, second_group, separator=','):
    group_one = first_group.split(separator)
    group_two = second_group.split(separator)
    general = list(set(group_one).intersection(group_two))


    return sorted(general)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, separator='|'))