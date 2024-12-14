###################################
# READ DATA INPUT
###################################
def read_file_input (file_name: str):

  text_file = open(file_name, "r")
  lines = text_file.read().split('\n')
  lines.remove("")
  text_file.close()
  return lines

def buil_board(lines:list):
  
  new_list = []

  for line in lines:
    new_list.append(list(line))


  X_MAX = len(new_list[0])
  Y_MAX = len(new_list)
  
  print ("MAxxs:  ", X_MAX, Y_MAX)

  return new_list

def find_trail_head(board: list):
  new_coord = []

  for y in range(0, len(board)):
    for x in range(0, len(board[y])):
      if board[y][x] == "0":
        new_coord.append((x, y))
  return new_coord

def find_path(board, trail_head, part2):

  print(f"Finiding a path starting from ({trail_head})")
  val_start = "0"
  val_end = "9"
  x, y = trail_head
  trace(trail_head, board, val_start, x, y)
  
  if part2:
    print ("found part 2", found_paths_list, len(found_paths))
    return len(found_paths_list)
  else:
    print ("found part 1", found_paths, len(found_paths))
    return len(found_paths)

def trace(trail_head, board, val_end, x, y):

  #print("checking", x, y)

  if x == -1 or y == -1 or x >= X_MAX or y >= Y_MAX:
    return

  try:
    
    current_value = board[y][x]
   # print("trying", current_value, val_end)

  except:
    current_value = "-1"
   # print("Exception", x, y)
    return 
  
  
  if current_value == val_end and current_value == "9":
    print(f"Reached a nine, saving its location ({x},{y}) and its starting point {trail_head}")
    found_paths.add((x,y))
    found_paths_list.append((x,y))
    return (x, y)

  if current_value == ".":
   # print("Found a dot")
    return 
  
  if current_value == val_end : # need to check prev value and if difference is 1
    
    #print ("ok on the right track")
    #print("Going left", x-1, y)
    trace(trail_head, board, str(int(current_value) + 1), x-1, y) 
   # print(" come back", x, y, "going up", x, y-1)
    trace(trail_head, board, str(int(current_value) + 1), x, y-1)  
    #print(" come back", x, y, "going right", x+1, y)
    trace(trail_head, board, str(int(current_value) + 1), x+1, y)
    #print(" come back", x, y, "going down", x, y+1)
    trace(trail_head, board, str(int(current_value) + 1), x, y+1)
    #print(" come back", x, y)
    return 

found_paths = set()
found_paths_list = []

X_MAX = 99
Y_MAX = 99
def main():

  lines = read_file_input("./data/day10_input.txt")
  board = buil_board(lines)
  trail_heads = find_trail_head(board)
  #print(trail_heads)
  number_of_unique_end = 0
  number_of_unique_paths = 0
  for trail_head in trail_heads:
    found_paths.clear()
    found_paths_list.clear()
    number_of_unique_paths = number_of_unique_paths + find_path(board, trail_head, True)
    number_of_unique_end = number_of_unique_end + find_path(board, trail_head, False)


  print ("Day 10 Part 1 solution: ", number_of_unique_end)
  print ("Day 10 Part 2 solution: ", number_of_unique_paths)


main()    

