n = int(input())


person_list = []
for i in range(n):
    student_input = input().split()
    person_list.append((student_input[0], student_input[1],))

for i in range(n):
    print(*person_list[i])

for i in range(n):
    if person_list[i][1] == '4' or person_list[i][1] == '5':
        print(*person_list[i])