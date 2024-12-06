def read_file_input (file_name):

    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lines.remove("")
    text_file.close()
    return lines

lines = read_file_input("./2024/data/day2_input.txt")

def successive_difference(report):

    diff = []
    for i in range(1, len(report)):
        diff.append(report[i] - report[i-1])
    
    return diff


def is_report_safe(diff):

    all_positive = True if max(diff) > 0 and min(diff) > 0 else False
    all_negative = True if max(diff) < 0 and min(diff) < 0 else False
    between_1_and_3 = True if max([abs(val) for val in diff]) >= 1 and max([abs(val) for val in diff]) <= 3 else False

    return (1 if ((all_positive or all_negative) and between_1_and_3) else 0)

def is_safe_with_dampener(report: list):

    for i in range(0, len(report)):
        list_to_try = report.copy()
        del list_to_try[i]
        diff = successive_difference(list_to_try)
        if is_report_safe(diff) == 1:
            break

    return is_report_safe(diff)

safe_report_count = 0
safeish_report_count = 0

for report in lines:
    report = report.split(' ')
    report = list(map(int, report))
    diff = successive_difference(report)
    safe_report_count = safe_report_count + is_report_safe(diff)
    
    if is_report_safe(diff) == 0:
        safeish_report_count = safeish_report_count + is_safe_with_dampener(report)
    
    #print(report, diff, is_report_safe(diff))

print("Day 2 Part 1 solution: ", safe_report_count)
print("Day 2 Part 2 solution: ", safe_report_count + safeish_report_count)