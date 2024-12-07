###################################
# READ DATA INPUT
###################################
def read_file_input (file_name: str):

  text_file = open(file_name, "r")
  lines = text_file.read().split('\n')
  lines.remove("")
  text_file.close()
  return lines

def read_input (file_name: str):
  lines = read_file_input(file_name)
  return [list(line) for line in lines]

###################################
# Initiate Position
###################################
def get_current_position(map: list, search: str):

  for line in map:
    if any(e == search for e in line):
      x = line.index(search)
      y = map.index(line)

  return (x,y)

def get_obstacle_position(map: list, search: str):

  line_no = 0
  obstacles = []

  for line in map:
    col_no = 0
    for e in line:
      if e == search:
        x = col_no
        y = line_no
        obstacles.append((x,y))
      col_no = col_no + 1
 
    line_no = line_no + 1
  return obstacles

def add_to_dictionary(visited_location_dict, key):
  
  if key in visited_location_dict :
    visits = visited_location_dict[key]
    visited_location_dict[key] = visits + 1
  else:
    visited_location_dict[key] = 1

  return visited_location_dict

def mark_move_on_map(x_from, x_to, y_from, y_to, visited_location_dict):

  if x_from == x_to:
    #moving vertically
    for b in range(y_from, y_to+1):
      if b != -1:
          visited_location_dict = add_to_dictionary(visited_location_dict, str(x_from) + '_' +str(b))
          #print ("adding location vertical move", x_from, b)

    for b in range(y_to, y_from + 1):
      if b != -1:
          visited_location_dict = add_to_dictionary(visited_location_dict, str(x_from) + '_' +str(b))
          #print ("adding location vertical move", x_from, b)

  elif y_from == y_to:
    #moving horizontally
    for a in range(x_from, x_to+1):
      if a != -1:
          visited_location_dict = add_to_dictionary(visited_location_dict, str(a) + '_' +str(y_from))
          #print ("adding location horizontal move", a, y_from)
    for a in range(x_to, x_from+1):
      if a != -1:
          visited_location_dict = add_to_dictionary(visited_location_dict, str(a) + '_' +str(y_from))
          #print ("adding location horizontal move", a, y_from)
  return visited_location_dict

######  MOVE UP  ######
def move_up(visited_location_dict, x, y, obstacle_vector):

  new_pos_x = x
  #print(f'Moving up from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos < y]
  
  if len(valid_obstacles) != 0:
    first_obstacle = max(valid_obstacles)
  else:
    first_obstacle = -1
  
  #print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_y = -1
    next_action = "END"
    new_direction = ""
  else:
    new_pos_y = first_obstacle + 1
    next_action = "GO"
    new_direction = "RIGHT"
  
  visited_location_dict = mark_move_on_map(x, new_pos_x, y, new_pos_y, visited_location_dict)

  return (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict)

def move_down(visited_location_dict, x, y, obstacle_vector):
  new_pos_x = x
  #print(f'Moving down from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos > y]
  
  if len(valid_obstacles) != 0:
    first_obstacle = min(valid_obstacles)
  else:
    first_obstacle = -1
  
  #print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_y = MAX_Y
    next_action = "END"
    new_direction = ""
  else:
    new_pos_y = first_obstacle - 1
    next_action = "GO"
    new_direction = "LEFT"
  
  visited_location_dict = mark_move_on_map(x, new_pos_x, y, new_pos_y, visited_location_dict)

  return (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict)


def move_left(visited_location_dict, x, y, obstacle_vector):

  new_pos_y = y
  #print(f'Moving left from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos < x]
  
  if len(valid_obstacles) != 0:
    first_obstacle = max(valid_obstacles)
  else:
    first_obstacle = -1
  
  #print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_x = -1
    next_action = "END"
    new_direction = ""
  else:
    new_pos_x = first_obstacle + 1
    next_action = "GO"
    new_direction = "UP"
  
  visited_location_dict = mark_move_on_map(x, new_pos_x, y, new_pos_y, visited_location_dict)

  return (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict)
  

def move_right(visited_location_dict, x, y, obstacle_vector):

  new_pos_y = y
  #print(f'Moving right from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos > x]
  
  if len(valid_obstacles) != 0:
    first_obstacle = min(valid_obstacles)
  else:
    first_obstacle = -1
  
  #print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_x = MAX_X
    next_action = "END"
    new_direction = ""
  else:
    new_pos_x = first_obstacle - 1
    next_action = "GO"
    new_direction = "DOWN"
  
  visited_location_dict = mark_move_on_map(x, new_pos_x, y, new_pos_y, visited_location_dict)

  return (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict)

def start_moving(map : list, obstacles : list, current_position : tuple, direction: str, visited_location_dict: dict):

  MIN_X = 0
  MIN_Y = 0
  MAX_X = len(map[0]) - 1
  MAX_Y = len(map) - 1

  # print (f'Map Size: {MAX_X + 1} x {MAX_Y + 1}')
  # print ('Obstacles position: ', obstacles)
  # print ('Current position: ', current_position)
  # print ('Current direction: going', direction)

  loop = False
  action = "GO"

  while action != "END" and not loop :
  
    if direction == "UP":
      (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict) = move_up(visited_location_dict, current_position[0], current_position[1], 
                                                                        [ely for elx,ely in obstacles if elx == current_position[0]])
    elif direction == "DOWN":
      (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict) = move_down(visited_location_dict, current_position[0], current_position[1],  
                                                                        [ely for elx,ely in obstacles if elx == current_position[0]])
    elif direction == "LEFT":
      (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict) = move_left(visited_location_dict, current_position[0], current_position[1], 
                                                                        [elx for elx,ely in obstacles if ely == current_position[1]])
    else:    
      (new_pos_x, new_pos_y, new_direction, next_action, visited_location_dict) = move_right(visited_location_dict, current_position[0], current_position[1], 
                                                                        [elx for elx,ely in obstacles if ely == current_position[1]])

    current_position = (new_pos_x, new_pos_y)
    direction = new_direction
    action = next_action
    # check if we have been here before
    key = str(new_pos_x) + "_" + str(new_pos_y)
    if key in visited_location_dict:
      if visited_location_dict[key] > 4:
        loop = True

  
  #print('Ending position', current_position)
  #print('Visited', visited_location_set)
  
  return (len(visited_location_dict), loop)



def start():

  loop_count = 0
  direction = "UP"
  visited_loc = 0 

  visited_location_dict = {} 
  #part 1
  (visited_loc, loop) = start_moving(map, obstacles, current_position, direction, visited_location_dict)
  
  #part 2
  #print(obstacles)
  
  for idx, row in enumerate(map):
    print('Processing line: ', idx)
    for idy, col in enumerate(row):
      if col == ".":
        # add obstacle
        new_obstacle = [(idy, idx)]
        
        loop = False
        visited_location_dict.clear()
        visited_loc_part2 = 0
        direction = 'UP'
        (visited_loc_part2, loop) = start_moving(map, obstacles + new_obstacle, current_position, direction, visited_location_dict)
        if loop == True:
          loop_count = loop_count + 1
  
  return (visited_loc, loop_count)


map = read_input("./2024/data/day6_input.txt")  
#print(map[37])  
current_position = get_current_position(map, "^")
#print(current_position)
obstacles = get_obstacle_position(map, "#")
#print(obstacles)

MIN_X = 0
MIN_Y = 0
MAX_X = len(map[0]) - 1
MAX_Y = len(map) - 1


# Start Finding Solution
(how_many_places, how_many_obstructions_for_loop) = start()

print ("Day 6 solution Part 1:", how_many_places)
print ("Day 6 solution Part 2:", how_many_obstructions_for_loop)

# for each element on the map, if no obstacles, add obsatcle and calculate
