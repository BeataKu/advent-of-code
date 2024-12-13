import re 
###################################
# READ DATA INPUT
###################################
def read_file_input (file_name: str):

  text_file = open(file_name, "r")
  lines = text_file.read().split('\n')
  lines.remove("")
  text_file.close()
  return lines

def multiply (occurence: str): 
  value = 0
  
  regex = r"\d+"
  numbers = re.findall(regex, occurence)
  value = int(numbers[0]) * int(numbers[1])

  return value

def main(part1 : bool = True):


  lines = read_file_input("./data/day3_input.txt")
  total = 0

  if part1:
    regex = r"(?:mul\()(\d+,\d+)(?:\))"

    for line in lines:
      occurences = re.findall(regex, line)
      #print(occurences)
      for occurence in occurences:
        total = total + multiply(str(occurence))

    print ("Day 3 Part 1 solution: ", total)
  else:
    regex = r"(?:mul\()(\d+,\d+)(?:\))|(do\(\))|(don\'t\(\))"

    do_op = True
    
    for line in lines:
      occurences = re.findall(regex, line)

      for occurence in occurences:

        
        for col in list(occurence):

          if col == "don't()":
            do_op = False
            break
          
          elif col == "do()":
            do_op = True
            break

        if do_op and occurence[0] != "":
          total = total + multiply(str(occurence[0]))

    print ("Day 3 Part 2 solution: ", total)

  return


main(True)    
main(False)    

