def find_common_participants(group1, group2, separator=','):
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common_participants = participants1.intersection(participants2)
    sorted_common_participants = sorted(common_participants)
    return sorted_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)
