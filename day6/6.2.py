import string

questions = set(list(string.ascii_lowercase))


def open_questions(raw):
    with open(raw) as f:
        groups = f.read().split('\n\n')
        return groups


def check_total_answers(groups: list):
    total = 0
    for group in groups:
        sets = []
        person = group.split()
        for p in person:
            current_set = set()
            for x in p:
                if x in questions:
                    current_set.add(x)
            sets.append(current_set)

        tempset = set.intersection(*sets)
        total += len(tempset)

    return total


qa_data = open_questions('cd.txt')
print(
    f'For each group, the number of questions to which everyone answered "yes" is {check_total_answers(qa_data)}')
