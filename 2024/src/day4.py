
filename = "./data/day4_input.txt"

text_file = open(filename, "r")
lines = text_file.read().split('\n')
text_file.close()

# find divider in data between page_ordering_rules and page updates
index_divider = lines.index('')

page_ordering_rules = lines[0 : index_divider]
page_updates = lines[index_divider + 1:]

middle_element = []

for update in page_updates:

    update = update.split(',')
    # get list of correctly ordered updates
    try:
        for page in update:
            current_index = update.index(page)
            for next_page in update[current_index + 1: ]:
                rule = page + "|" + next_page
                
                if rule not in page_ordering_rules:
                    raise ValueError('Rule not met')
        
        middle_element.append(int(update[int((len(update)-1)/2)]))
    except ValueError:
        continue


print("Part 1: ", sum(middle_element))



