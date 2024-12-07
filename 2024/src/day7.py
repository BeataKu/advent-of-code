###################################
# READ DATA INPUT
###################################
def read_file_input (file_name: str):

  text_file = open(file_name, "r")
  lines = text_file.read().split('\n')
  lines.remove("")
  text_file.close()
  return lines

def prod (a: int, b: int):
  return a*b

def sum (a: int, b: int):
  return a+b

def concat (a: int, b: int):
  return int(str(a)+str(b))

def generator_list_of_operators_itertools (list_length, operations : list):
  
  from itertools import product
  return list(product(operations, repeat=list_length))


# function to check if test value can be calibrated with numbers
def test_numbers (test_value: int, numbers: int, use_concat: bool = False):

  if use_concat == False:
    operators = generator_list_of_operators_itertools (len(numbers)-1, [prod, sum])
  else:
    operators = generator_list_of_operators_itertools (len(numbers)-1, [prod, sum, concat])

  for operator in operators:
    #iterate through operators
    total = 0
    for index in range(0, len(operator)):
      if index == 0:
        total = int(numbers[index])
      total = operator[index](total, int(numbers[index+1]))

    if total == test_value:
      #print (f"Testing if {test_value} can be achieved with {numbers} ... it can {total}")
      return total
  return 0

def main():

  lines = read_file_input("./2024/data/day7_input.txt")

  total_calibration_result_part1 = 0
  total_calibration_result_part2 = 0

  for line in lines:

    index_divider = line.index(':')
    test_value = line[0 : index_divider]
    numbers = line[index_divider + 1:]
    numbers = numbers.split(' ')
    numbers.remove("")
    
    total_calibration_result_part1 = total_calibration_result_part1 + test_numbers (int(test_value), numbers, False)
    total_calibration_result_part2 = total_calibration_result_part2 + test_numbers (int(test_value), numbers, True)

  print ("Day 7 Part 1 solution: ", total_calibration_result_part1)
  print ("Day 7 Part 2 solution: ", total_calibration_result_part2)


main()    

