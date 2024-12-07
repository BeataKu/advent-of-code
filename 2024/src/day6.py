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

visited_location_set = set()

def mark_move_on_map(x_from, x_to, y_from, y_to):

  if x_from == x_to:
    #moving vertically
    for b in range(y_from, y_to+1):
      if b != -1:
          visited_location_set.add((x_from, b))
          #print ("adding location vertical move", x_from, b)

    for b in range(y_to, y_from + 1):
      if b != -1:
          visited_location_set.add((x_from, b))
          #print ("adding location vertical move", x_from, b)

  elif y_from == y_to:
    #moving horizontally
    for a in range(x_from, x_to+1):
      if a != -1:
          visited_location_set.add((a, y_from))
          #print ("adding location horizontal move", a, y_from)
    for a in range(x_to, x_from+1):
      if a != -1:
          visited_location_set.add((a, y_from))
          #print ("adding location horizontal move", a, y_from)
  return

######  MOVE UP  ######
def move_up(map, x, y, obstacle_vector):

  new_pos_x = x
  print(f'Moving up from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos < y]
  
  if len(valid_obstacles) != 0:
    first_obstacle = max(valid_obstacles)
  else:
    first_obstacle = -1
  
  print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_y = -1
    next_action = "END"
    new_direction = ""
  else:
    new_pos_y = first_obstacle + 1
    next_action = "GO"
    new_direction = "RIGHT"
  
  map = mark_move_on_map(x, new_pos_x, y, new_pos_y)

  return (new_pos_x, new_pos_y, new_direction, next_action, map)

def move_down(map, x, y, obstacle_vector):
  new_pos_x = x
  print(f'Moving down from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos > y]
  
  if len(valid_obstacles) != 0:
    first_obstacle = min(valid_obstacles)
  else:
    first_obstacle = -1
  
  print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_y = MAX_Y
    next_action = "END"
    new_direction = ""
  else:
    new_pos_y = first_obstacle - 1
    next_action = "GO"
    new_direction = "LEFT"
  
  map = mark_move_on_map(x, new_pos_x, y, new_pos_y)

  return (new_pos_x, new_pos_y, new_direction, next_action, map)


def move_left(map, x, y, obstacle_vector):

  new_pos_y = y
  print(f'Moving left from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos < x]
  
  if len(valid_obstacles) != 0:
    first_obstacle = max(valid_obstacles)
  else:
    first_obstacle = -1
  
  print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_x = -1
    next_action = "END"
    new_direction = ""
  else:
    new_pos_x = first_obstacle + 1
    next_action = "GO"
    new_direction = "UP"
  
  map = mark_move_on_map(x, new_pos_x, y, new_pos_y)

  return (new_pos_x, new_pos_y, new_direction, next_action, map)
  

def move_right(map, x, y, obstacle_vector):

  new_pos_y = y
  print(f'Moving right from {x},{y}')
  valid_obstacles = [pos for pos in obstacle_vector if pos > x]
  
  if len(valid_obstacles) != 0:
    first_obstacle = min(valid_obstacles)
  else:
    first_obstacle = -1
  
  print ('Obstacles on a way pos y:', first_obstacle)
  
  if first_obstacle == -1:
    new_pos_x = MAX_X
    next_action = "END"
    new_direction = ""
  else:
    new_pos_x = first_obstacle - 1
    next_action = "GO"
    new_direction = "DOWN"
  
  map = mark_move_on_map(x, new_pos_x, y, new_pos_y)

  return (new_pos_x, new_pos_y, new_direction, next_action, map)

def start_moving(map : list, obstacles : list, current_position : tuple, direction: str):

  MIN_X = 0
  MIN_Y = 0
  MAX_X = len(map[0]) - 1
  MAX_Y = len(map) - 1

  print (f'Map Size: {MAX_X + 1} x {MAX_Y + 1}')
  print ('Obstacles position: ', obstacles)
  print ('Current position: ', current_position)
  print ('Current direction: going', direction)

  loop = False
  action = "GO"

  while action != "END" and not loop :
  
    if direction == "UP":
      (new_pos_x, new_pos_y, new_direction, next_action, map) = move_up(map, current_position[0], current_position[1], 
                                                                        [ely for elx,ely in obstacles if elx == current_position[0]])
    elif direction == "DOWN":
      (new_pos_x, new_pos_y, new_direction, next_action, map) = move_down(map, current_position[0], current_position[1],  
                                                                        [ely for elx,ely in obstacles if elx == current_position[0]])
    elif direction == "LEFT":
      (new_pos_x, new_pos_y, new_direction, next_action, map) = move_left(map, current_position[0], current_position[1], 
                                                                        [elx for elx,ely in obstacles if ely == current_position[1]])
    else:    
      (new_pos_x, new_pos_y, new_direction, next_action, map) = move_right(map, current_position[0], current_position[1], 
                                                                        [elx for elx,ely in obstacles if ely == current_position[1]])

    current_position = (new_pos_x, new_pos_y)
    direction = new_direction
    action = next_action

  print('Ending position',current_position)
  print('Visited', visited_location_set)
  
  return len(visited_location_set)

def start():
  direction = "UP"
  return start_moving(map, obstacles, current_position, direction)


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
how_many_places = start()
print ("Day 6 solution Part 1:", how_many_places)