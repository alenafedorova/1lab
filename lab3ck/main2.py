def find_common_participants(group1, group2, separator=","):

    participants_group1 = group1.split(separator)
    participants_group2 = group2.split(separator)
    common_participants = []
    for participant in participants_group1:
        if participant in participants_group2:
            common_participants.append(participant)
    common_participants = list(set(common_participants))
    common_participants.sort()

    return common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общие участники: {common_participants}")