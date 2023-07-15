reportCard = list()
while True:
    name = str(input('Name: '))
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    averageGrade = (grade1 + grade2) / 2
    reportCard.append([name, [grade1, grade2], averageGrade])
    answer = str(input('Do you want to continue? [\033[1;32mY\033[m/\033[1;31mN\033[m] '))
    if answer in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-' * 26)
for i, s in enumerate(reportCard):
    print(f'{i:<4}{s[0]:<10}{s[2]:>8.1f}')
while True:
    print('-' * 35)
    operation = int(input('Show grades of which student? (\033[1;31m999\033[m interrupts): '))
    if operation == 999:
        print('\033[1;31mShutting down...\033[m')
        break
    if operation <= len(reportCard) - 1:
        print(f'Grades of \033[4;35m{reportCard[operation][0]}\033[m are \033[4;32m{reportCard[operation][1]}\033[m')
print('\033[1;32m<<< WELCOME >>>\033[m')
