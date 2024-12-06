def read_file_input (file_name):

    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    text_file.close()
    return lines


lines = read_file_input("./data/day1_input.txt")

first = []
second = []

lines.remove("")

for line in lines:
    first.append(line.split('   ')[0])
    second.append(line.split('   ')[1])

first.sort()
second.sort()

sum_distance = 0
for i in range(len(first)):
    sum_distance = sum_distance + (abs(int(first[i]) - int(second[i])))

print("Part 1 solution: ", sum_distance)

similarity_score = 0
for i in range(len(first)):
    similarity_score = similarity_score + int(first[i]) * second.count(first[i])

print("Part 2 solution: ", similarity_score)