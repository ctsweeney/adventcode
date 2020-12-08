import string

questions = set(list(string.ascii_lowercase))

with open("cd.txt") as f:
    groups = f.read().split("\n\n")

    total = 0
    people = len(groups)
    for group in groups:
        answers_set = []
        person = group.split()
        answers_set = set([x for a in person for x in a if x in questions])
        total += len(answers_set)

    print(
        f'For each group, the number of questions to which anyone answered "yes" is {total}')
